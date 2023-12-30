## Hacking the Human Vasculature in 3D

### 17기 김연규, 18기 최유민, 18기 김송성

3D Hierarchical Phase-Contrast Tomography (HiP-CT)로 촬영된 인체의 신장 데이터에서 혈관을 분할. 
 
-> 몸 전체의 혈관 구조 사진을 완성하는 것 도움
-> 인체 조직의 혈관의 크기, 모양, 패턴 등에 대한 연구자의 이해 도움

## 3가지 접근
### SAM
Segment Anything 모델 사용. Pre trained 모델 사용.
2D slice된 이미지를 이용하여 각 이미지별로 segmentation. 


### U-Net
의료 분야에서 가장 많이 사용되는 모델인 U-Net 사용
이미지 slice를 모델에 넣는 것이 아닌 5개 slice를 합쳐서 모델 입력에 사용(2.5D)
Backbone 모델을 바꾸기, Loss function, image size 등 변경해 사용해가며 모델 성능 측정

![image](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/95427125/6b095c40-73bc-4a54-aa04-aec3e30f507c)


### SCNAS
3D 의료 segmentation에서 사용되는 neural architecture search Framework
SubVolume 단위로 모델 입력에 사용.
Inference 시에도 각 Subvolume에 대해서 Inference 이후, 총 Volume을 재구성

