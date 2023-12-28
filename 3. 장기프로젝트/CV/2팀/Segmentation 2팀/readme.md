# Segment vasculature in 3D scans of human kidney

KUBIG CV2팀 / Segmentation 2팀 : 17기 김예은, 17기 임종우, 18기 원준혁

## 프로젝트 목표
HIP-CT로 촬영한 3D Kidney image에서 주어진 혈관 이미지 데이터를 효과적으로 segmentation하기

## 사용 데이터
사람의 3D 신장 데이터를 2D로 slice한 데이터들 : 데이터 종류별 특징 존재(dense, voi 등)
- visualization
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0b51e84c-ae92-445e-abb6-a766fbaae435/bab5293b-fb60-44cc-947c-62ae409b1265/Untitled.png)

## train / inference
1. 2D
- Unet 구조 및 attention Unet 구조
- random 과정 등의 data augmentation
- batch size 및 threshold 등 조건 변경 후 train
  
2. 2.5D
- Unet 구조 기반
- slice된 이미지들을 연결 -> 학습 시간 축소
- random 과정 등의 data augmentation
- 이미지를 grayscale로 로드 및 특정 data를 valid로 설정
- learning rate, backbone 모델 등 변경하면서 train

## 결과
2D
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0b51e84c-ae92-445e-abb6-a766fbaae435/c145e983-9afd-4448-b419-ebc46233fc6e/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0b51e84c-ae92-445e-abb6-a766fbaae435/acaa0ff8-8340-49a3-9988-b8f46056f85a/Untitled.png)

2.5D
![학습률.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0b51e84c-ae92-445e-abb6-a766fbaae435/17195aa6-23de-4e3a-8bde-a82a430855df/%ED%95%99%EC%8A%B5%EB%A5%A0.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0b51e84c-ae92-445e-abb6-a766fbaae435/7f04f0b6-e192-4c2a-afef-ce1cf53c3324/Untitled.png)
