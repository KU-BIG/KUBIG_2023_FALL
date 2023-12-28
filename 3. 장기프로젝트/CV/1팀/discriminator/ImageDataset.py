from torch.utils.data import Dataset
import os
from PIL import Image

class ImageDataset(Dataset):
    def __init__(self, image_folder, transform, label):
        self.image_paths = [os.path.join(image_folder, f"{i}.jpg") for i in range(1, 21)]  # 1부터 20까지의 이미지 경로
        self.labels = [label for _ in range(20)]  
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        image = Image.open(image_path).convert('RGB')
        image = self.transform(image)
        return image, self.labels[idx]
    
class ImageDataset_1(Dataset):
    def __init__(self, image_paths, labels, transform):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        label = self.labels[idx]
        image = Image.open(image_path).convert('RGB')
        image = self.transform(image)
        return image, label