# 2023 가을 KUBIG CONTEST - ML 분반 2팀
## 팀원
18기 이준복, 신인수, 진서연, 정하윤

## 주제: 감귤 착과량 예측
https://dacon.io/competitions/official/236038/overview/description

## 목표
감귤나무의 나무 생육 상태, 엽록소 및 새순 정보로부터 감귤 착과량 예측한다. 
train set의 경우 수목(나무)별 착과량이 측정되어 있는 supervised learning, regression 문제에 해당. 

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

## 중점
train 데이터로 pycaret, autoML 등으로 분석 모델을 설정하더라도 R2가 높게, MAE가 낮게 나왔다. 이는 착과량과 새순 변수가 상관계수가 매우 높기 때문인 것으로 보인다. 그래서 본 프로젝트에서는 변수선택법으로 모델에 사용할 변수들을 최대한 정확히 선정하는 것으로 목표를 설정했다.

기존 변수들과 더불어, 착과량과 상관계수가 높은 새순에 대해 대푯값으로(평균, 중위수 등) 파생 변수들을 만들었다. 이렇게 기존 변수 182개 + 파생변수 15개 = 총 197개의 변수들을 가지고 변수선택법을 적용한다.

변수 선택법은 다음과 같이 나뉜다.
- Filter method: mutual information (mutual_info_regression), linear regression F test (f_regression), chi-square test for feature selection (chi2)
- Embedded method: LASSO, Ridge, Elastic net
- Wrapper method: forward selection, backward elimination, recursive feature elimination

이런 방법들을 적용했을 때 모델 특성과 적절한 변수선택법을 선정하여 이를 바탕으로 회귀 모델을 적용하였다.

wrapper method의 경우, 변수 subset을 구하고 각 조합마다 모델에 적용해야 하기 때문에, 변수가 많은 데이터 특성상 선택되지 않았다. 또한, wrapper method은 모델 훈련 과정에 적용되기 때문에, 미리 변수를 고르고자 하는 목표에 맞지 않기도 했다.

따라서 filter method과 embedded method 중에서 가장 적절한 변수들을 골라낸 f_regression과 LASSO를 선택하였다. 
**(둘 중 무엇이 좋은지는 결론이 난 후 작성)**

## 모델
pycaret 사용 시 Gradient Boosting Regressor가 결과가 좋게 나왔기 때문에, 본 모델을 사용한다.
