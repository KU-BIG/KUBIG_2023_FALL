# 🌏 Proposals for the Future Direction of South Korea’s Official Development Assistance
**🥇 대상(1위) 수상**

![첨부 1  KDIS 공모전_한국의 미래 ODA 시행방향에 대한 제언_1](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/104672441/278abd70-e05f-4094-a12b-f6b0d730b3ab)
---
# Abstract
- 한국은 1995년 세계은행의 원조대상국을 벗어나 2009년부터 DAC의 회원국이 되어 공적개발원조를 진행
- 한국의 ODA(Official development assistance, 공적개발원조) 규모는 2010년 10억 달러 규모를 넘어서 2016년 **20억 달러 규모를 초월**
- 언론 보도에 따르면 한국의 ODA 규모는 매년 증가하는 추세이나 규모만으로 ODA의 실적을 평가할 수는 없음
  - 국별 프로그램 원조는 2010년 54.3%에서 2021년 47.5%로 감소
  - CPA 비중이 다른 회원국에 비해 크게 낮아 **ODA의 효율성 측면에서 최하위 평가**
  - 한국의 경제 지표(GNI, 물가상승률, 경제성장률)을 고려했을 때 **실질적 측면에서의 증액 여부는 불투명**
  - 비교적 낮은 무상원조 비율, 정책/집행 담당 기관 분리로 인한 원조 분절화, 예비검토제에 기인한 느린 정책 추진 등 **여러 정책적 문제**
  - 실제로 UN의 선진국 ODA/GNI(국민총소득 대비 원조액) 목표치인 0.7%에 비해 한국은 2022년 0.17%로 **30개 회원국 중 16위**
- 이에 ODA 상황 개선, 예산의 효율적인 집행 및 ODA의 효용 극대화를 위한 **데이터 기반의 심층적 분석 수행**
  - 국내외 ODA와 관련한 여러 분야의 정량적 지표 수집, 전처리, EDA
  - ODA 규모 포함 여러 지표를 고려하여 정책 참조 국가를 선정, 그들의 ODA 정책을 비교분석
  - 단기/장기 관점에서 한국의 ODA 정책의 방향 제시
# Process
## 1. Feature Importance
- Purpose: 42개 국가의 50여 개 지표(% of GDP)를 수집하여 ODA 규모에 영향을 미치는 주요 변수를 추출
- Task: N년의 Data로 N+1년의 ODA 규모를 예측하는 회귀 문제로 정의
- Method: Filter Method, Embedded Method, Wrapper Method를 활용해 유의미한 변수 추출, Baseline Model(Random Forest, Linear Regression)의 성능(MAE, MSE, $R^2$)으로 변수 검증
## 2. Clustering
- Purpose: 정량적인 지표를 활용해 국가를 군집화해 정책을 참조할 만한 국가를 선정
- Task: 고차원 정량적 지표 반영 `(1) ODA 규모 Data`, `(2) ODA 관련 Data`, `(3) 주요 변수가 포함된 Data` 관점에서 국가를 나누는 문제로 정의
- Method: Hierarchical Clustering(Complete Link) 활용, Elbow Method로 군집 개수 선정
# Results
- Feature Importance 결과 13개 주요 변수 선정, $R^2$ 0.9816 달성하여 ODA 규모를 결정짓는 국가 지표 확정 
- Clustering 결과 아래 3개국을 Reference 국가로 선정
  - 일본: 높은 절대적 규모, 중간 상대적 규모, 상업주의적 모델, 한국과 같은 문화권
  - 덴마크: 낮은 절대적 규모, 높은 상대적 규모, 인도주의적 모델, 이상적인 ODA 수행
  - 캐나다: 중간 절대적 규모, 중간 상대적 규모, 한국과 같은 Cluster
- 한국과 세 국가의 정책을 분석하고 비교(Report 참고)
# Conclusion
While Canada, Japan, and Denmark manage their ODA under a single agency, Korea’s MOFAT(Ministry of Foreign Affairs and Trade, 외교통상부) and MOSF(Ministry of Strategy and Finance, 기획재정부) manage Grants and Loans, respectively. This leads to fragmentation and inefficiency, so a single agency should be in charge of ODA, with a single perspective from planning to evaluation. Denmark has the best ODA in terms of indicators, but it is difficult to accept due to the different public sentiment, culture, and geographical features of ODA with Korea. Therefore, it is necessary to take advantage of Canada and Japan’s policy, which has the same culture as Korea, and make practical improvements, and ultimately aim for Denmark’s ODA. As a specific policy, we propose that Korea’s ODA should aim to ensure efficiency in aid distribution and management through the alignment of executive agencies, secure transparency through annual reports, and suggest an increase in the ODA/GNI ratio.
