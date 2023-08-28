
<h1 align="center"> 
2023-FALL KUBIG Contest
<h1/>

## 주제

제목 : "Using LoRA for AI Profiling: Dynamic Persona Generation through Diffusion Modeling"

주제 설명 : 생동감있게 움직이는 개인화된 AI 프로필을 생성한다.
- diffusion model을 베이스 모델로 사용하고 personal feature는 LoRA fine tuning을 통해 구현한다. 
- 생성된 AI 프로필의 움직임은 animatediff를 활용한다.


## Team

<KUBIG 2023-FALL> 

17기 임청수 18기 전병우 최유민

## Fine Tuning Method

1. textual inversion
2. LoRA fine tuning
원하는 대상이 포함된 20장의 이미지를 구축한 후 이미지마다 대응되는 캡션을 설정한다. 데이터셋이 구축되면 stable diffusion을 training_model로 하여 repeat, epochs, network_dim, network_alpha 등의 hyperparameter를 조절하며 LoRA를 생성한다.
[Guide - LoRA Style Training](https://civitai.com/questions/158/guide-lora-style-training)


4. LoRA with Dreambooth

## text2gif
AnimateDiff를 활용하여 text로 gif 파일을 생성한다. 적절한 base model과 직접 style을 학습한 LoRA 모델, 원하는 정도의 motion을 표현하는 motion_module을 구축한다. prompt, n_prompt engineering을 통해 tuning을 진행한다.


## 최종 결과물

(유민)

## 개발환경
<img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white"><img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white">

<img src="https://img.shields.io/badge/Gradio-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white"><img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white">

<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">


  
  
