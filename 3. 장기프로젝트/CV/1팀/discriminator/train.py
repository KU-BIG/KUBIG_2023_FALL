import torch
import torch.nn as nn
from discriminator import Discriminator, load_image
from ImageDataset import ImageDataset, ImageDataset_1
from tqdm import tqdm
from PIL import Image
from torchvision import transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([
    #transforms.Resize((256, 256)),
    transforms.ToTensor(),
    #transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

## Folder 지정하고 dataset 만들기
# real_dataset = ImageDataset('/home/tjddms9376/cv/data/real/', transform, 1)  # 진짜 이미지는 레이블 1
# fake_dataset = ImageDataset('/home/tjddms9376/cv/data/fake/', transform, 0)  # 가짜 이미지는 레이블 0

# combined_dataset = torch.utils.data.ConcatDataset([real_dataset, fake_dataset])

# batch_size = 4 
# dataloader = DataLoader(combined_dataset, batch_size=batch_size, shuffle=True)


# path 직접 지정
real_image_paths = [f'/home/tjddms9376/cv/data/real/{x}.jpg' for x in range(1000)]
fake_image_paths = [f'/home/tjddms9376/cv/data/fake/{x}.png' for x in range(1000)]
real_labels = [1 for _ in real_image_paths]
fake_labels = [0 for _ in fake_image_paths]

dataset = ImageDataset_1(real_image_paths + fake_image_paths, real_labels + fake_labels, transform)

batch_size = 4
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)


### Training

discriminator = Discriminator()

criterion = nn.BCELoss()
optimizer = torch.optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

num_epochs = 10

for epoch in tqdm(range(num_epochs)):
    for images, labels in tqdm(dataloader):
        optimizer.zero_grad()

        real_labels = torch.ones(labels.size(0), 1, dtype=torch.float)
        fake_labels = torch.zeros(labels.size(0), 1, dtype=torch.float)

        outputs = discriminator(images)
        labels = labels.float().view_as(outputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

# Training Loop (single image)
# for epoch in tqdm(range(num_epoch)):
    
#     optimizer.zero_grad()
#     real_labels = torch.ones(1, 1)  
#     real_output = discriminator(real_artwork)
#     real_loss = criterion(real_output, real_labels)
#     real_loss.backward()

#     fake_labels = torch.zeros(1, 1)  
#     fake_output = discriminator(generated_artwork)
#     fake_loss = criterion(fake_output, fake_labels)
#     fake_loss.backward()

#     optimizer.step()

torch.save(discriminator.state_dict(), f'/home/tjddms9376/cv/discriminator/pretrained/model_1000figure.pth')

