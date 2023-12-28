from albumentations import (
    Compose, Resize, HorizontalFlip, VerticalFlip, Rotate, 
    RandomBrightnessContrast, HueSaturationValue, Blur, OpticalDistortion, 
    GridDistortion, ElasticTransform
)
from PIL import Image
import numpy as np
import os
from tqdm import tqdm

transform = Compose([
    Resize(width=256, height=256),
    HorizontalFlip(p=0.5),
    VerticalFlip(p=0.5),
    Rotate(limit=45, p=0.5),
    RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.5),
    HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20, p=0.5),
    Blur(blur_limit=3, p=0.5),
    OpticalDistortion(p=0.5),
    GridDistortion(p=0.5),
    ElasticTransform(alpha=1, sigma=50, alpha_affine=50, p=0.5)
])

total_image = []

# 이미지 로드
for i in tqdm(range(1,139)):
    image_path = f'/home/tjddms9376/cv/data/Salvador_Dali/Salvador_Dali_{i}.jpg'
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_np = np.array(image)

    save_path = '/home/tjddms9376/cv/data/real'

    for s in range(20):
        augmented_image_np = transform(image=image_np)['image']
        augmented_image = Image.fromarray(augmented_image_np.astype(np.uint8))
        total_image.append(augmented_image)

for k in range(len(total_image)):
    total_image[k].save(os.path.join(save_path, f'{s}.jpg'))
print("All augmented images have been saved.")