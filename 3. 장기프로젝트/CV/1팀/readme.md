# DALL-E를 찾아라!
20세기 초반에 가장 영향력 있던 초현실주의 화가 'Salvador Dali'는 꿈과 현실을 혼합한 독특한 예술 작품으로 현재까지 많은 사랑을 받고 있는 인물입니다. 그의 작품은 상상력과 창의성을 토대로 비현실적인 이미지를 통해 깊은 인상을 남기는 것이 특징입니다.
OpenAI는 Salvador Dali처럼 상상력이 풍부한 이미지를 생성해내라는 의미와 픽사의 애니메이션 영화 'WALL-E'에서 영감을 받아, text-to-image generation model인 DALL-E 모델을 개발했습니다. DALL-E 모델은 텍스트 기반의 설명을 바탕으로 복잡하고 상세한 이미지를 생성하는 인공지능 모델입니다.

저희 CV 1팀은 텍스트를 통해 다양한 이미지를 생성해낼 수 있는 DALL-E 모델을 통해 Computer Vision 분야에서 주목받고 있는 classification, detection 등의 다양한 task들을 진행했습니다.

## Task 소개
저희가 진행한 task는 크게 3가지입니다. 
- Classification : 주어진 이미지에 포함된 주요 내용이나 객체를 식별하고, 해당 이미지가 어떤 범주에 속하는지 결정합니다.
- Detection : 이이미지 내에 특정 객체가 존재하는지 확인하고, 단순히 객체의 존재 여부뿐만 아니라 해당 객체의 위치와 크기를 정확히 파악합니다.
- Discriminator : 주어진 이미지가 실제 작품의 이미지인지, generative model을 통해 생성한 이미지인지 결정합니다.

### Classification

초현실주의 화가 Dali가 그린 그림에는 다양한 object들이 비현실적인 형태로 존재하는 경우가 많습니다. 해당 object가 무엇을 의미하는지 사람이 식별하는 것은 쉽지만, 컴퓨터에게도 과연 쉬운 일일까요?
저희 팀은 Vision Transformer(ViT)와 EfficientNet과 같은 대표적인 image classification 모델을 통해 컴퓨터가 물체를 잘 분류할 수 있는지 살펴보았습니다.

### Detection

이미지 안에 어떤 object가 존재하는 지 확인했으므로 이제 해당 object가 어디에 위치하는 지를 파악하는 작업을 진행합니다. 비현실적인 형태의 object들을 detection하기 위해 다양한 방법론을 고려합니다. 
또한 Detection이 완료된 이미지는 새로운 synthetic data로 사용할 수 있습니다.

### Discriminator

Synthetic data로 사용할 때, 해당 이미지에 대한 fake or real 여부가 중요할 수 있습니다. 생성된 새로운 fake image를 실제 화가의 작품으로 인식하고 모델을 훈련시킨다면 원하는 결과를 얻지 못할 수 있으므로 discriminator를 통해 해당 이미지에 대한 fake or real 여부를 결정합니다. 
