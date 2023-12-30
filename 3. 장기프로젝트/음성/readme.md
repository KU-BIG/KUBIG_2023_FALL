# 침수자 프로젝트
팀원 : 16기 신인섭, 천원준, 17기 임청수, 홍예빈

❓ 침수자 : 침착맨 수호자의 줄임말로, 침착맨 유튜브의 편집자를 뜻함  
📌 목표 : 침착맨 영상 중 다중 화자인 영상 음원을 받아, 화자를 분리하고, 각 화자에 따른 음성인식을 통해 최종적으로 자막을 생성하는 것을 목표! 

## Pipline
![image](https://github.com/KU-BIG/KUBIG_2023_FALL/assets/80189765/78e111b6-4028-438a-be58-67ad7f3f9e69)

## Code
1. sepformer_final.ipynb : 화자 분리 코드
2. Denosing.ipynb : 화자 분리 이후 노이즈 처리
3. whisper_finetuning_korean_chimsuja.ipynb : 음성인식

그 외
- TOLD_final : Told 시도
- speaker identification : 분리된 음성(ex 음성1, 음성2)를 어떤 화자(ex. 침착맨, 김풍)인지 구분하기 위한 코드 
