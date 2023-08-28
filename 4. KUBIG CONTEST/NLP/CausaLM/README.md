# CausaLM : 인과추론 기반 감성 분석

## Introduction

딥러닝 모델들은 구조가 없는 데이터에 의존하는 분야에서 자주 사용되며 복잡한 계층 구조와 비선형 활성화 함수 등으로 인해 모델의 해석 가능성과 해석력을 갖추지 못한 경우가 대다수입니다. 따라서, 의료와 사회과학 같은 분야에서 효과적인 개념 기반 설명을 위한 도구가 필수가 되었고, 이로 인해 도입된 개념 중에 하나가 바로 **'Causal concept-based explanation'** 입니다.
그 중에서 'counterfactual examples'을 생성하여 실제 모델의 예측 값과 대조적 예제의 예측 값을 비교해보는 방법이 가장 일반적인 방법입니다. 하지만, counterfactual examples을 생성하는 과정이 어렵기 때문에 이에 대한 새로운 방안으로 본 연구에서 **'Counterfactual text representation'** 을 활용한 방법을 제시합니다.

CausaLM은 텍스트 데이터에서 인과 관계를 파악하고, 기존의 인과 추론 방법에서 사용하는 counterfactual example 대신 counterfactual text representation을 활용한 모델입니다. 이 프로젝트는 Sentiment classification을 인과 추론 기반으로 다루고 있으며 다양한 masking 방법과 concept 개념을 도입하여 결과를 도출하고 있습니다.

## Pre-requisite

**1. gitclone으로 필요한 파일들을 설치**
- `git clone https://github.com/amirfeder/CausaLM.git`
- `git clone https://github.com/ ~`

**2. 가상환경 설치 및 환경 구성**
- Create the CausaLM conda environment : `conda activate causalm_gpu_env.yml`
- Download the _adjectives_ datasets and place them in the `./datasets` folder
- `pip install pytorch_lightning==0.5.3.2`
- `transformers==2.7.0` `apex==0.1` `cupy-pre` `spacy==2.3.8`
- `python -m spacy download en_core_web_lg`

※ Make sure the CAUSALM_DIR variable in `constants.py` is set to point to the path where the CausaLM datasets are located.

※ CAUSALM_DIR에 사용되는 변수들은 `constants.py`에 명시되어 있습니다.

## GuideLine
### Stage 2 training

다음 스크립트를 차례대로 실행해주세요.

- `./data_utils/Data_generation.ipynb` : 데이터 생성
- `./data_utils/bias_dataset.ipynb` : Aggressive / Balanced / Gentle 데이터 버전 생성
- `./MLM_adjtask.ipynb`
- `./IMA_adjtask.ipynb`

This will save the intervened BERT language model which treats for Adjectives treatment(IMA), with the option of adding the PoS tagging control task.

### Stage 3 training and test
- `./train_adj.ipynb [--pretrained_control]`

This will train and test all the Sentiment classifiers for the full experimental pipeline for Adjectives treatment, with the option of utilizing the Stage 2 model which employs the PoS tagging control task.


## Resource

CausaLM: Causal Model Explanation Through Counterfactual Language Models
https://arxiv.org/pdf/2005.13407v5.pdf

