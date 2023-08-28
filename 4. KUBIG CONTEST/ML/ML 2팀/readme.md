# 2023 가을 KUBIG CONTEST - ML 분반 2팀
## 팀원
18기 신인수, 이준복, 진서연, 정하윤

## 주제: 감귤 착과량 예측
https://dacon.io/competitions/official/236038/overview/description

## 목표
본 프로젝트의 목표는 감귤나무의 나무 생육 상태, 엽록소 및 새순 정보로부터 감귤 착과량을 예측하는 것임
Train Set에는 Target 변수인 수목(나무)별 착과량이 포함되어 있기 때문에 본 프로젝트는 supervised learning, regression 문제에 해당됨 

## 변수
- ID : 과수나무 고유 ID
- 착과량(int) : 실제 감귤 착과량 (Target)
- 나무 생육 상태 Features (4개):
  * 수고(m), 수관폭1(min), 수관폭2(max), 수관폭 평균(수관폭1과 수관폭2의 평균)
    - Column에서 단위가 'm'로 기입되어 있으나, 실제 데이터는 cm 단위로 기입되어 있음
- 새순 Features (89개):
2022년 09월 01일 ~ 2022년 11월 28일에 일별 측정된 새순 데이터
- 엽록소 Features (89개):
2022년 09월 01일 ~ 2022년 11월 28일에 일별 측정된 엽록소 데이터

## 프로젝트 진행 방식
가장 처음에는, 4명이 각각의 방식으로 전체 모델링 과정(EDA ~ 모델 적용)을 수행하였음
이후, 각각 진행한 방식을 공유하고 논의하여 추후 개선하면 좋을 방식을 결정하였음
주 2~3회 정도 온라인 회의를 진행하였으며, 회의에서 결정된 내용을 바탕으로 각각 본인의 모델링 과정을 개선해오는 방식으로 프로젝트를 진행하였음

## 프로젝트 방향성
처음에 모델링 과정을 pycaret 라이브러리와 autoML 라이브러리로 진행하였을 때, 어떠한 모델을 활용하더라도 모델 성능이 좋게 나왔음 (R2가 매우 높게(0.96 이상), MAE(30-35)가 낮게 나옴)
이는 Target 변수인 착과량과 독립 변수인 새순 변수가 상관계수가 매우 높기 때문인 것으로 파악하였음 
그래서 본 프로젝트에서는 기존의 변수 이외에도 새로운 파생 변수를 추가하고, 변수선택법을 통해 모델에 사용할 변수들을 최종적으로 결정하는 데에 주안점을 두었음

## 데이터 EDA 과정
Train Set의 변수의 개수가 184개로, 각 변수에 대해 깊은 EDA 과정을 수행하기 쉽지 않았음
그래서, 가장 먼저 전체 변수를 대상으로 각 변수의 데이터 분포와 Target 변수인 착과량 변수와의 상관관계를 확인하고 이후 유의미한 결과를 보인 변수에 대해 보다 깊은 EDA 과정을 수행하였음
각 변수의 데이터 분포를 확인하여 이상치를 제거할 것인지 하지 않을 것인지를 결정하였고, 착과량 변수와의 상관관계를 확인하여 어떠한 변수를 중점적으로 활용할 것인지 결정하였음
결과적으로, 모든 변수에 대해 이상치를 제거하지 않았으며 새순 변수의 상관계수가 매우 높게 도출되어 새순 변수를 집중적으로 활용하는 것으로 방향성을 수립함

## 데이터 전처리 과정
가장 먼저, 착과량과 상관계수가 높은 새순에 대한 대푯값(평균, 중위수, 범위 등)을 바탕으로 파생 변수들을 만들었음
결과적으로, 기존의 독립 변수 182개 + 파생변수 15개 = 총 197개의 변수들을 가지고 변수선택법을 적용하였음

변수를 축소하는 방법에는 변수 추출(feature extraction)과 변수 선택(feature selection)이 있음
변수 추출 방법을 통해 변수의 개수를 줄이는 경우에는, 새롭게 추출된 변수에 대한 해석이 쉽지 않기 때문에, 변수 선택 방법을 활용하였음

변수 선택법은 다음과 같이 구분할 수 있음
- Filter method: mutual information (mutual_info_regression), linear regression F test (f_regression), chi-square test for feature selection (chi2), Spearman correlation, feature importance
- Embedded method: LASSO, Ridge, Elastic net
- Wrapper method: forward selection, backward elimination, recursive feature elimination

이런 방법들을 활용하여, 본 데이터셋에 가장 적절한 변수들을 선택하고자 하였음
위의 3가지 방법 중 Wrapper method의 경우, 변수 subset을 구하고 각 조합마다 모델에 적용해야 하기 때문에 일반적으로 변수가 많은 데이터셋에는 사용되지 않는 방법이라고 파악하였음
또한 wrapper method은 모델 훈련 과정에 적용되기 때문에, 모델 훈련 전 전처리 과정에서 미리 변수를 선택하고자 하는 방향성에 부합하지 않았음

따라서 Filter method과 Embedded method을 활용하였으며, 이 중에서 가장 적절한 변수들을 골라낸 f_regression 방법과 LASSO 방법을 선택하였음
2개의 변수 선택법을 통해 결정된 변수들을 바탕으로 모델 적용 과정을 진행하였음

## 모델 적용
f_regression 방법과 LASSO 방법을 거쳐 선택된 변수들을 바탕으로 pycaret 라이브러리를 활용하였으며, 2개의 방법 모두 Gradient Boosting Regressor 모델의 성능이 가장 높게 도출되었음
GBR는 hyperparameter tuning이 필요하기 때문에, 2개의 모델 모두 hyperparameter tuning을 진행하였음

GradientBoostingRegressor에서 튜닝이 필요한 hyperparameter들은 다음과 같음

- learning_rate
- max_depth
- max_features
- min_samples_leaf
- min_samples_split
- n_estimators
- subsample

위의 hyperparameter에 대해 튜닝시킨 모델을 바탕으로 Test Set에 적용하여 착과량을 예측하고, 예측한 결과를 데이콘에 제출하여 최종적인 결과를 확인하는 과정을 거쳤음
