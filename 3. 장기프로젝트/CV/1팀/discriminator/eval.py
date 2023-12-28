from discriminator import Discriminator, load_image
import torch
from PIL import Image

def evaluate_image(model, image, label):
    with torch.no_grad():
        output = model(image)
        predicted_label = 'Real' if output.item() > 0.5 else 'Fake'
        print(f"Label: {label}, Predicted: {predicted_label}, Confidence: {output.item()}")


real_artwork = load_image('/home/tjddms9376/cv/data/real_1/2.png').unsqueeze(0)  # Add batch dimension
generated_artwork = load_image('/home/tjddms9376/cv/test.png').unsqueeze(0)

# real_path = '/home/tjddms9376/cv/data/real/3.jpg'
# fake_path = '/home/tjddms9376/cv/data/fake/2.png'

# real_artwork = Image.open(real_path)
# generated_artwork = Image.open(fake_path)
# if real_artwork.mode != 'RGB':
#     real_artwork = real_artwork.convert('RGB')
# if generated_artwork.mode != 'RGB':
#     generated_artwork = generated_artwork.convert('RGB')

loaded_model = Discriminator()
loaded_model.load_state_dict(torch.load('/home/tjddms9376/cv/discriminator/pretrained/model_1000figure.pth'))
loaded_model.eval()  

evaluate_image(loaded_model, generated_artwork, 'Fake')
evaluate_image(loaded_model, real_artwork, 'Real')
