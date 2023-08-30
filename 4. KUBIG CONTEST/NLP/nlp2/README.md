<div align="center">
    <img src="https://github.com/2023KUBIGNLP2/Malang_news/assets/104672441/482e7c0e-3406-4afe-bb2e-0670ff1b011a" alt="말랑" width="" height="50">
</div>

# 말랑뉴스: 딱딱한 뉴스를 말랑말랑하게
길고 복잡한 뉴스 원문을 짧게 요약하고 주요 키워드를 질답 형태로 풀어 설명해주는 서비스입니다.  
딱딱한 문장에서 다른 말투로 변경이 가능하며, 키워드에 대해 질문하는 정도를 조절 가능합니다.   
어려운 단어가 많은 IT/과학 분야 또는 금융 분야에 특화해 Fine-tuning 되었습니다.  
[Team Notion](https://enchanted-gum-e41.notion.site/KUBIG-NLP-Project-659dac81a4f34a7883022319551751dd?pvs=4)  
[시연 영상](https://youtu.be/0Mwv_NaXx0E)
## 서비스 이용하기
**`malang_news.py`에 본인의 Huggingface API Key, OpenAI API Key를 입력해야 합니다.**
```
$ pip install -r requirements.txt
$ streamlit run streamlit/malang_news.py
```
> 1. 원하는 뉴스의 URL 입력 (네이버 뉴스에 최적화)
> 2. Inference 기다리고 결과 받아보기
- 말투 변환 및 키워드 질문 정도 조절 가능
- **아직 모델을 불러오는 중이에요.** 안내 문구 출력 시 조금 뒤 다시 시도
- **뉴스를 찾을 수 없어요.** 안내 문구 출력 시 url이 올바른지 확인
## 프로젝트 구조
```
nlp2/
│
├── crawler/
|   ├── headline_crawler_final.py
|   ├── headline_crawler_onlybs.py
|   ├── newneek_crawler.ipynb
|   ├── news_crawler_final.py
|   └── 네이버뉴스_크롤링.ipynb
│
├── model/
│   ├── BART/
|   |   ├── KoBART_navernews.ipynb
|   |   ├── 생성요약_KoBART.ipynb
|   |   └── 추출요약_KoBART.ipynb
|   | 
│   ├── KeyBERT/
|   |   └── keyword_extract.ipynb
│   |
|   └── causalLM/
|       ├── GPTtrain.py
|       └── koalpaca_fine-tuning.ipynb
|
├── preprocessing/
|   ├── json2csv.ipynb
|   ├── newneek_preprocessing.ipynb
|   └── news_preprocessing_labeling.ipynb
|  
└── streamlit/
    ├── malang_news.py
    └── utils.py
```
## Dataset
- 네이버뉴스 - 금융
- 네이버뉴스 IT/과학 헤드라인 뉴스
- [Korean SmileStyle Dataset](https://github.com/smilegate-ai/korean_smile_style_dataset)
## Model
### 문서 요약
- [KoBART](https://huggingface.co/gogamza/kobart-base-v1)
### 키워드 추출
- KeyBERT
- [KoBERT](https://huggingface.co/skt/kobert-base-v1)
### 키워드 질답
- [GPT3.5 turbo](https://platform.openai.com/)
### 말투 변환
- [KoBART](https://huggingface.co/gogamza/kobart-base-v1)
- [kobart-text-style-transfer](https://huggingface.co/heegyu/kobart-text-style-transfer)
## 사용 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=for-the-badge&logo=Pytorch&logoColor=white"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white">
