# KubigCVPoseEstiProject
## 주제 : 태권도 품새 동작 식별 프로젝트
mp4 파일 내에 있는 태권도 품새 동작을 식별한 후 어떤 동작인지 알려주는 프로젝트이다.
## 팀원
16기 박민규, 17기 김지윤, 백서경, 임종우

### 1. Data extract
AI Hub의 고양시 태권도 데이터에서 training dataset 을 추출한다.

training dataset은 원천데이터와 원천데이터의 pose 정보에 대한 라벨링데이터로 구성되어있으며, 원천데이터를 추출한다. 원천데이터는 태권도 동작을 시연한 mp4의 비디오 원시데이터를 1초당 120프레임씩 추출한 jpg파일로 이루어져있다. 

원천데이터는 동작을 기준으로 분류되어있으며, 총 64가지 동작에 대해 48명의 데이터가 주어진다. 
48명은 성비 1:1, 6명의 선수와 42명의 훈련생으로 이루어져있어 다양성의 확보를 위해 **동작별로 선수 6명과 훈련생 14명 총 20명의 데이터를 "표준"을 기준으로 추출**, 총 20*64=1280장을 얻는다.

한 사람이 시연한 태권도 동작 데이터의 구성은 아래와 같다.
![image](https://github.com/MinkyuRamen/KubigCVPoseEstiProject/assets/108858246/088ddcfd-8f7a-4eb5-a3a6-39bf04484664)
[**다시점(8개 방향)** 카메라 이미지 + **동작시작점 – 중간점 – 종료점 이미지**로 구분하여 데이터 가공] 되어있다.

⇒ 8*3=24개의 이미지가 있으며, 여기서 **전방&측면 시점의 종료점 이미지**을 추출한다.

단 발차기 동작의 경우 따로 추출한다.

ex) 앞차고 압굽혀 찌르기 ⇒ 앞차기, 압굽혀 찌르기 따로 분류 후 라벨링 진행

### 2. Data Preprocessing
- ViTPose 로 keypoint 추출
- Flipping Augmentation 적용
- 샘플 당 x, y 좌표의 평균 및 표준편차로 Standardization 적용

### 3. Classification
추출한 고양시 태권도 데이터에서 각각 동작별 분류를 진행한다.

#### - Without CNN
 1. RandomForest -> acc 0.969 (w/ tabular data)
 2. Feedforward Neural Network -> acc 0.71 (w/ tabular data)
 3. Multi-Layer Perceptron -> acc 0.94 (w/ tensor transformation)

#### - With CNN
tabular data -> 2d array 로 변환

 4. CNN with Conv1d -> acc 0.94
 5. CNN with Conv2d -> acc 0.95
 6. Pre-trained CNN (MobileNet_v2) -> acc 0.91

#### accuracy 정리
|model|acc|
|-----|---|
|RF|0.969|
|Neural Net|0.71|
|MLP|0.94|
|Conv1d|0.94|
|Con2d|0.95|
|MobileNet_v2|0.81|

### 4. Video process
태극 7장 영상(1분)을 0.2초단위(프레임)으로 자른다. 총 약 300장의 이미지를 추출한다.

추출한 이미지를 easy-ViTPose를 태워 관절 위치를 알아내고, 이를 바탕으로 어떤 동작인지 분류한다.
![image](https://github.com/MinkyuRamen/KubigCVPoseEstiProject/assets/108858246/7323ff4b-a5b1-4653-9da1-aa019f8a7530)
