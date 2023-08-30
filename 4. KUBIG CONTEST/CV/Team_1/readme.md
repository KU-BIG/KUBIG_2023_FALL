# :recycle: PET CAN do anything

### :two_men_holding_hands: CV Team 1 17기 문성빈, 강민채, 김희준, 이서연

<br>

## :mag: Introduction

- 문제의식: 대규모행사에서 고질적인 문제로 꼽히는 분리수거 문제
- 캔, 플라스틱, 유색페트, 무색페트, 일반쓰레기를 real time으로 Object Detection하여 분리수거에 기여

<br>

## :open_file_folder: Data
- AI Hub 제공 "재활용품 분류 및 선별 데이터"
- bounding box 처리된 알류미늄캔, 플라스틱, 무색단일 페트병, 유색단일 페트병 이미지 각 1,000개씩 사용

<br>

## :chart_with_upwards_trend: Train
- YOLOv5 Model Backbone 사용
- Dataset Train/Test/Val split 
- YOLOv5s pretrained Weights 사용
- Linux / NVIDIA TITAN RTX
- epoch: 100 / batch size: 16


<br>

## :computer: Environment
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=PyTorch&logoColor=white"/><br>
  <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat&logo=Google Colab&logoColor=white"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Linux-FCC624?style=flat&logo=Linux&logoColor=white"/>
