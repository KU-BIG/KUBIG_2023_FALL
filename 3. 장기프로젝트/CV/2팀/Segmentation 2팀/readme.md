# Segment vasculature in 3D scans of human kidney

KUBIG CV2팀 / Segmentation 2팀 : 17기 김예은, 17기 임종우, 18기 원준혁

## 프로젝트 목표
HIP-CT로 촬영한 3D Kidney image에서 주어진 혈관 이미지 데이터를 효과적으로 segmentation하기

## 사용 데이터
사람의 3D 신장 데이터를 2D로 slice한 데이터들 : 데이터 종류별 특징 존재(dense, voi 등)

- visualization



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


2.5D

