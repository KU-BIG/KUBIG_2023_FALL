
<h1 align="center"> 
2023-FALL KUBIG Contest
<h1/>

## 주제

제목 : "Using LoRA for AI Profiling: Dynamic Persona Generation through Diffusion Modeling"

주제 설명 : 생동감있게 움직이는 개인화된 AI 프로필을 생성한다.
- diffusion model을 베이스 모델로 사용하고 personal feature는 LoRA fine tuning을 통해 구현한다. 
- 생성된 AI 프로필의 움직임은 animatediff를 활용한다.

## 발표자료

https://docs.google.com/presentation/d/1iNbBWvNVnd1eHdtF1XFE_Lw_XWexw9oj/edit?usp=sharing&ouid=107811774026611155765&rtpof=true&sd=true



## Team

<KUBIG 2023-FALL> 

17기 임청수 18기 전병우 최유민

## Fine Tuning Method

1. textual inversion
2. LoRA fine tuning
   
LoRA(Low-Rank Adaptation of Large Language Models)란?

LoRA는 PEFT(Parameter Effecient Fine-Tuning)의 기법 중 하나이다. Pre-trained model의 weight는 고정한 채로, 몇 개의 dense(fc) layer만 학습시켜 downstream task의 연산량을 줄일 수 있다. 

LoRA를 이용한 Stable diffusion Fine Tuning
원하는 대상이 포함된 20장의 이미지를 구축한 후 이미지마다 대응되는 캡션을 설정, stable diffusion을 training_model로 repeat, epochs, network_dim, network_alpha 등 hyperparameter를 조절하여 LoRA를 생성

- [Guide - LoRA Style Training](https://civitai.com/questions/158/guide-lora-style-training)


3. LoRA with Dreambooth
DreamBooth란?

text-to-image 모델의 personalization 기법 중 하나.

대상의 몇 장의 사진으로 text-to-image 모델을 fine tuning 하여 대상의 특징을 학습한다.

다른 personalization 기법에 비해 학습된 데이터상의 포즈, 배경 이외에도 다양한 사진을 생성해낼 수 있다.

DreamBooth - LoRA장점은? 

기존 드림부스 기법은 모델 전체를 fine tuning하여 기존 Stable Diffusion 모델 만큼의 용량(2Gb)이 필요하다. LoRA 기법을 파일은 평균 100Mb정도로 사용자들 간의 모델 이동이 수월하다.

## text2gif

1. AnimateDiff를 활용하여 text로 gif 파일을 생성
   
2. 적절한 base model과 직접 style을 학습한 LoRA 모델, 원하는 정도의 motion을 표현하는 motion_module을 구축

3. Sampler, Step, Clip skip, CFG scale 등의 파라미터 조정으로 최적의 퀄리티를 만들어내는 값 찾기
   
4. prompt, n_prompt engineering을 통해 tuning을 진행


## 최종 결과물

1. LoRA + Stable diffusion
   
![toonyou_image_grid](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/95427125/be71c0f0-f7ab-4c86-835e-11b39e49139f)


2. majicmixRealistic_betterV2V25

![00027-1793506252](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/95427125/ccd3ca00-c008-4974-bebd-6f399b79bf29)
![v6-6_4](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/95427125/da709963-0614-4404-b598-5d06bf03be83)
![v1-6-_5](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/95427125/97b05ab3-00f5-4c78-af03-a0df6a68255b)

3. ToonYou

![00059-2118982731](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/95427125/e0362c22-2c32-4888-9729-3a267e242c66)
![00064-1843641884](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/95427125/2266bb23-5a1a-4e61-8d3a-8f551de6b8ba)


### 학습 설정
Best quality(유민 LoRA 모델, gif 이미지) 생성 설정 공유
LoRA Training : 15 high quality image, repeat 40 , epoch 6 , step 3600, optimizer : adam8bit, learning rate 등 나머지 parameter는 기본 설정과 동일 / 학습 이미지의 퀄리티가 굉장히 중요
AnimateDiff 생성 설정 : clip skip 2, step 45, sampler DDIM, CFG scale 15, motion module : 14
DDIM sampler를 사용하지 않으면 gif가 두 이미지로 생성되게 됨.
CFG scale : 너무 낮으면 이미지에서 회색 빛이 너무 많이 돌고, 높으면 glitter 현상 발생
motion module 14가 15에 비해 이미지 움직임이 많고, watermark가 없음.

## 개발환경
<img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white"><img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white">

<img src="https://img.shields.io/badge/Gradio-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white"><img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white">

<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">


  
  
