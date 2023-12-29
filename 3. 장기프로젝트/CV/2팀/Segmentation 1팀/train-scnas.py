import os
import random
from tqdm import tqdm
import numpy as np
import gc
import time
from collections import defaultdict
import copy
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.optim import lr_scheduler
import torch.optim as optim
from dataset import RandomVolumetricDataset, ToDevice, RandomRotationNd, RandomFlipNd, RandomRot90Nd
import torchvision.transforms as T
from scnas import ScNas 



class CFG:
    seed          = 42
    debug         = False # set debug=False for Full Training
    exp_name      = 'baseline'
    output_dir    = './checkpoint/'
    model_name    = 'scnas'

    train_bs      = 4
    valid_bs      = 16
    volume_shape  = [128, 128, 128]
    epochs        = 200
    n_accumulate  = max(1, 64//train_bs)
    
    lr            = 2e-5
    
    # learning rate scheduler
    scheduler     = 'ReduceLROnPlateau'
    min_lr        = 1e-10
    T_max         = 100
    T_0           = 25
    warmup_epochs = 0
    
    # optimizer : Adam optimizer
    wd            = 0
    betas = (0.5, 0.999)

    n_fold        = 5
    num_classes   = 1
    device        = torch.device("cuda:3" if torch.cuda.is_available() else "cpu")

    gt_df = "../data/gt.csv"
    data_root = "../data/blood-vessel-segmentation/"

    train_groups = ["train/kidney_1_dense", "train/kidney_2", "train/kidney_3_dense"]
    valid_groups = ["train/kidney_2"]

    loss_func     = "DiceLoss"

    data_transforms = T.Compose((ToDevice(device = device), RandomRot90Nd(3), RandomFlipNd(3)))



def set_seed(seed = 42):
    '''Sets the seed of the entire notebook so results are the same every time we run.
    This is for REPRODUCIBILITY.'''
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    # When running on the CuDNN backend, two further options must be set
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    # Set a fixed value for the hash seed
    os.environ['PYTHONHASHSEED'] = str(seed)
set_seed(CFG.seed)


# DataLoader
train_path = [os.path.join(CFG.data_root, group) for group in CFG.train_groups]
valid_path = [os.path.join(CFG.data_root, group) for group in CFG.valid_groups]

train_dataset = RandomVolumetricDataset(train_path, shape=CFG.volume_shape, length=1000, transform=CFG.data_transforms)
valid_dataset = RandomVolumetricDataset(valid_path, shape=CFG.volume_shape, length=100, transform=CFG.data_transforms)

train_loader = DataLoader(train_dataset, batch_size=CFG.train_bs, num_workers=0, shuffle=True, drop_last=False)
valid_loader = DataLoader(valid_dataset, batch_size=CFG.valid_bs, num_workers=0, shuffle=False)


def build_model(device):
    model = ScNas(num_feature = 8, num_layers = 6, num_multiplier = 2, num_classes = 1, use_bridge = True, input_channel = 1)
    model.to(device)
    return model


model = build_model(CFG.device)


class JaccardDistanceLoss3D(nn.Module):
    def __init__(self, smooth=1e-6):
        super(JaccardDistanceLoss3D, self).__init__()
        self.smooth = smooth

    def forward(self, y_pred, y_true):
        y_pred = torch.sigmoid(y_pred)

        intersection = torch.sum(torch.min(y_pred, y_true), dim=(1, 2, 3, 4))
        union = torch.sum(torch.max(y_pred, y_true), dim=(1, 2, 3, 4))

        jaccard_score = (intersection + self.smooth) / (union + self.smooth)
        return 1 - jaccard_score.mean()
    

class DiceLoss3D(nn.Module):
    def __init__(self, smooth=1e-6):
        super(DiceLoss3D, self).__init__()
        self.smooth = smooth

    def forward(self, y_pred, y_true):
        y_pred = torch.sigmoid(y_pred)

        # Flatten the tensors to [batch_size, -1]. 
        # This way, all spatial dimensions (depth, height, width) are flattened into one dimension.
        y_pred_flat = y_pred.view(y_pred.size(0), -1)
        y_true_flat = y_true.view(y_true.size(0), -1)

        # Compute the intersection and the union
        intersection = 2.0 * (y_pred_flat * y_true_flat).sum(1)
        union = y_pred_flat.sum(1) + y_true_flat.sum(1)

        # Compute the Dice coefficient (score) and loss
        dice_score = (intersection + self.smooth) / (union + self.smooth)
        dice_loss = 1 - dice_score

        # You might want to return the mean or sum of the losses over the batch
        return dice_loss.mean()

    

JaccardLoss = JaccardDistanceLoss3D()
DiceLoss = DiceLoss3D()

def criterion(y_pred, y_true):
    if CFG.loss_func == "JaccardDistanceLoss":
        return JaccardLoss(y_pred, y_true)

    elif CFG.loss_func == "DiceLoss":
        return DiceLoss(y_pred, y_true)
    else:
        raise ValueError("No recognized loss function specified in CFG.loss_func")
    
    
def dice_coef(y_true, y_pred, thr=0.5, dim=(2,3), epsilon=0.001):
    y_true = y_true.unsqueeze(1).to(torch.float32)
    y_pred = (y_pred>thr).to(torch.float32)
    inter = (y_true*y_pred).sum(dim=dim)
    den = y_true.sum(dim=dim) + y_pred.sum(dim=dim)
    dice = ((2*inter+epsilon)/(den+epsilon)).mean(dim=(1,0))
    return dice

def iou_coef(y_true, y_pred, thr=0.5, dim=(2,3), epsilon=0.001):
    y_true = y_true.unsqueeze(1).to(torch.float32)
    y_pred = (y_pred>thr).to(torch.float32)
    inter = (y_true*y_pred).sum(dim=dim)
    union = (y_true + y_pred - y_true*y_pred).sum(dim=dim)
    iou = ((inter+epsilon)/(union+epsilon)).mean(dim=(1,0))
    return iou


def fetch_scheduler(optimizer):
    if CFG.scheduler == 'CosineAnnealingLR':
        scheduler = lr_scheduler.CosineAnnealingLR(optimizer,T_max=CFG.T_max, 
                                                   eta_min=CFG.min_lr)
    elif CFG.scheduler == 'CosineAnnealingWarmRestarts':
        scheduler = lr_scheduler.CosineAnnealingWarmRestarts(optimizer,T_0=CFG.T_0, 
                                                             eta_min=CFG.min_lr)
    elif CFG.scheduler == 'ReduceLROnPlateau':
        scheduler = lr_scheduler.ReduceLROnPlateau(optimizer,
                                                   mode='min',
                                                   factor=0.1,
                                                   patience=10,
                                                   threshold=0.0001,
                                                   min_lr=CFG.min_lr,)
    elif CFG.scheduer == 'ExponentialLR':
        scheduler = lr_scheduler.ExponentialLR(optimizer, gamma=0.85)
    elif CFG.scheduler == None:
        return None
        
    return scheduler
optimizer = optim.Adam(model.parameters(), lr=CFG.lr, betas = CFG.betas , weight_decay=CFG.wd)
scheduler = fetch_scheduler(optimizer)


def train_one_epoch(model, optimizer, scheduler, dataloader, device, epoch):
    model.train()
    
    dataset_size = 0
    running_loss = 0.0
    
    # pbar = tqdm(enumerate(dataloader), total=len(dataloader), desc='Train ')
    for step, (images, masks) in enumerate(dataloader):         
        images = images.to(device, dtype=torch.float)
        masks  = masks.to(device, dtype=torch.float)
        
        batch_size = images.size(0)
        
        # with amp.autocast(enabled=True):
        y_pred = model(images)
        loss   = criterion(y_pred, masks)
        # loss = loss / CFG.n_accumulate

        loss.backward()
    
        optimizer.step()

        # Zero the parameter gradients
        optimizer.zero_grad()

        
                
        running_loss += (loss.item() * batch_size)
        dataset_size += batch_size
        
        epoch_loss = running_loss / dataset_size
        
        mem = torch.cuda.memory_reserved() / 1E9 if torch.cuda.is_available() else 0
        current_lr = optimizer.param_groups[0]['lr']
        # pbar.set_postfix( epoch=f'{epoch}',
        #                   train_loss=f'{epoch_loss:0.4f}',
        #                   lr=f'{current_lr:0.5f}',
        #                   gpu_mem=f'{mem:0.2f} GB')
    torch.cuda.empty_cache()
    gc.collect()
    return epoch_loss

@torch.no_grad()
def valid_one_epoch(model, dataloader, device, epoch):
    model.eval()
    
    dataset_size = 0
    running_loss = 0.0
    
    val_scores = []
    
    pbar = tqdm(enumerate(dataloader), total=len(dataloader), desc='Valid ')
    for step, (images, masks) in enumerate(dataloader):        
        images  = images.to(device, dtype=torch.float)
        masks   = masks.to(device, dtype=torch.float)
        
        batch_size = images.size(0)
        
        y_pred  = model(images)
        loss    = criterion(y_pred, masks)
        
        running_loss += (loss.item() * batch_size)
        dataset_size += batch_size
        
        epoch_loss = running_loss / dataset_size
        
        y_pred = nn.Sigmoid()(y_pred)
        val_dice = dice_coef(masks, y_pred).cpu().detach().numpy()
        val_jaccard = iou_coef(masks, y_pred).cpu().detach().numpy()
        val_scores.append([val_dice, val_jaccard])
        
        mem = torch.cuda.memory_reserved() / 1E9 if torch.cuda.is_available() else 0
        current_lr = optimizer.param_groups[0]['lr']
        # pbar.set_postfix(valid_loss=f'{epoch_loss:0.4f}',
        #                 lr=f'{current_lr:0.5f}',
        #                 gpu_memory=f'{mem:0.2f} GB')
    val_scores  = np.mean(val_scores, axis=0)
    torch.cuda.empty_cache()
    gc.collect()
    return epoch_loss, val_scores

def run_training(model, optimizer, scheduler, device, num_epochs):    
    if torch.cuda.is_available():
        print("cuda: {}\n".format(torch.cuda.get_device_name()))
    
    start = time.time()
    best_model_wts = copy.deepcopy(model.state_dict())
    best_loss      = np.inf
    best_epoch     = -1
    history = defaultdict(list)
    
    for epoch in range(1, num_epochs + 1): 
        gc.collect()
        print(f'Epoch {epoch}/{num_epochs}', end='')
        train_loss = train_one_epoch(model, optimizer, scheduler, 
                                           dataloader=train_loader, 
                                           device=CFG.device, epoch=epoch)
        
        # train loss plateau를 판단하여 lr 감소
        if scheduler is not None:
            scheduler.step(train_loss)

        val_loss, val_scores = valid_one_epoch(model, valid_loader, 
                                                 device=CFG.device, 
                                                 epoch=epoch)
        val_dice, val_jaccard = val_scores
        history['Train Loss'].append(train_loss)
        history['Valid Loss'].append(val_loss)
        history['Valid Dice'].append(val_dice)
        history['Valid Jaccard'].append(val_jaccard)        
        #print(f'Valid Dice: {val_dice:0.4f} | Valid Jaccard: {val_jaccard:0.4f}')
        print(f'Train Loss: {train_loss}')
        print(f'Valid Loss: {val_loss}')
        
        # deep copy the model
        if val_loss <= best_loss:
            print(f"Valid loss Improved ({best_loss} ---> {val_loss})")
            best_dice    = val_dice
            best_jaccard = val_jaccard
            best_loss = val_loss
            best_epoch   = epoch
            best_model_wts = copy.deepcopy(model.state_dict())
            PATH = CFG.output_dir+"best_epoch.bin"
            torch.save(model.state_dict(), PATH)
            print(f"Model Saved")
            
        last_model_wts = copy.deepcopy(model.state_dict())
        PATH = CFG.output_dir+"last_epoch.bin"
        torch.save(model.state_dict(), PATH)
            
        print(); print()
    
    end = time.time()
    time_elapsed = end - start
    print('Training complete in {:.0f}h {:.0f}m {:.0f}s'.format(
        time_elapsed // 3600, (time_elapsed % 3600) // 60, (time_elapsed % 3600) % 60))
    print("Best Loss: {:.4f}".format(best_loss))
    
    # load best model weights
    model.load_state_dict(best_model_wts)
    return model, history

def load_model(device, path):
    model = build_model(device)
    model.load_state_dict(torch.load(path))
    print(f'checkpoint from {path} loaded')
    return model

model = load_model(CFG.device, "./checkpoint/last_epoch.bin")

model, history = run_training(model, optimizer, scheduler,
                                device=CFG.device,
                                num_epochs=CFG.epochs)