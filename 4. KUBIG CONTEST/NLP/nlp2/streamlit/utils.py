import re
from ast import literal_eval
from kiwipiepy import Kiwi
import requests
import random


def excluding_text(modified_text):
    pattern1 = re.compile(r"\s\([^)]*\)")
    modified_text = re.sub(pattern1, " ", modified_text)
    pattern2 = re.compile(r"\([^)]*\)\s")
    modified_text = re.sub(pattern2, " ", modified_text)
    pattern3 = re.compile(r"\([^)]*\)")
    modified_text = re.sub(pattern3, "", modified_text)
    pattern4 = re.compile(r"\[[^\]]*\]")
    modified_text = re.sub(pattern4, "", modified_text)
    return modified_text


def preprocessing_text(text):
    modified_text = text.replace(". ", ".\n")
    modified_text = excluding_text(modified_text)
    modified_text = modified_text.split("\n")
    cleaned_sentences = []
    for sentence in modified_text:
        modified_sentence = re.sub(r"\s\s+", " ", sentence)
        modified_sentence = re.sub(r"“([^“”]+)”", r'"\1"', modified_sentence)
        modified_sentence = re.sub(r"‘([^‘’]+)’", r"'\1'", modified_sentence)
        modified_sentence = re.sub(r"[^\w\s.?!]", "", modified_sentence)
        if modified_sentence.strip():
            cleaned_sentences.append(modified_sentence.strip())
    return cleaned_sentences


def postprocessing_text(text):
    modified_text = re.sub(r"[^a-zA-Z0-9\s,.\?!\"'가-힣]", "", text).strip()
    return modified_text


def list2str(text):
    string = ""
    for i, st in enumerate(text):
        string += st
        if i < len(text) - 1:
            string += " "
    return string


def noun_extractor(text):
    results = []
    kiwi = Kiwi()
    result = kiwi.analyze(text)
    for token, pos, _, _ in result[0][0]:
        if len(token) != 1 and pos.startswith("N") or pos.startswith("SL"):
            results.append(token)
    return results


def query(API_URL, headers, payload, max_length=None):
    if max_length:
        payload["parameters"] = {"max_length": max_length}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def question_query(keyword):
    question_list = [
        "은(는) 뭐야?",
        "은(는) 뭐지?",
        "이(가) 궁금해!",
        "에 대해 설명해줘.",
        "에 대해 아는 게 없어...",
        "이(가) 뭔지 모르겠어.",
        "...?",
        "이(가) 뭔지 알아?",
        "은(는) 처음 듣는데...",
        "이(가) 뭔지 나만 몰라?",
        "은(는) 뭘까?",
    ]
    question = []
    prompt = "\n Read the article above and answer the following questions. All my questions begin with '(Q)' and all your answers start with '(A)'. Please explain as long as possible. Do not contain '(Q)' but only '(A)' in your answer. Please answer in Korean."
    real_question = ""
    for key in keyword:
        temp_key = key + random.choice(question_list)
        temp_key2 = "(Q) " + key + "의 일반적인 의미, 이 뉴스 기사에서의 의미? "
        question.append(temp_key)
        real_question += temp_key2
    real_question = prompt + real_question
    return question, real_question
