# KubigCVPoseEstiProject
## 주제 : 태권도 품새 동작 식별 프로젝트
mp4 파일 내에 있는 태권도 품새 동작을 식별한 후 어떤 동작인지 알려주는 프로젝트이다.

### data extract
AI Hub의 고양시 태권도 데이터에서 training dataset 을 추출한다.

** 서경님 보충설명 **

label은 총 64개로 구성되어 있으며, [다시점(8개 방향) 카메라 이미지 + 동작시작점 – 중간점 – 종료점 이미지로 구분하여 데이터 가공] 되어있다.

⇒ 하나의 시점당 총 8*3=24개의 이미지가 있으며, 여기서 **전방&측면 시점의 ‘종료점 이미지’**을 추출한다.

단 발차기 동작의 경우 따로 추출한다.

ex) 앞차고 압굽혀 찌르기 ⇒ 앞차기, 압굽혀 찌르기 따로 분류 후 라벨링 진행

### Data Preprocessing
- ViTPose 로 keypoint 추출
- Flipping Augmentation 적용
- 샘플 당 x, y 좌표의 평균 및 표준편차로 Standardization 적용

### Classification
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

### video process
태극 7장 영상(1분)을 0.2초단위(프레임)으로 자른다. 총 약 300장의 이미지를 추출한다.

추출한 이미지를 easy-ViTPose를 태워 관절 위치를 알아내고, 이를 바탕으로 어떤 동작인지 분류한다.

### project
전소미의 신곡 'Fast Forward' 뮤비에 등장하는 태권도 장면에서 각각의 동작이 어떤 동작인지 분류해낸다.
