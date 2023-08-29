import requests
from bs4 import BeautifulSoup
import argparse
import pandas as pd
import time
from tqdm import tqdm
import os
import datetime
import pytz
import re


def save_csv(news_infos, check_start, check_end, save_path, kst):
    print(f"..저장하는 뉴스의 번호: {check_start}-{check_end}..")
    print(f"..저장하는 뉴스의 개수: {len(news_infos)}..")
    now = datetime.datetime.now(kst)
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    df = pd.DataFrame(news_infos, columns=["title", "url"])
    df.to_csv(
        os.path.join(
            save_path,
            f"headline_{len(news_infos)}_{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}.csv",
        ),
        index=False,
    )
    print(
        f"저장 완료! 'news_{len(news_infos)}_{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}.csv'"
    )
    return list()


def headline_crawler(
    delay, save_every, section, start_iter, end_iter, header, save_path
):
    kst = pytz.timezone("Asia/Seoul")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    news_infos = []  # title, link
    check_start = start_iter
    # 2023년 8월 25일 기준 IT
    base_url = f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={section}#&date=%2000:00:00&page="
    headers = {"user-agent": header}

    for i in tqdm(range(start_iter, end_iter + 1)):
        req = requests.get(f"{base_url}{i}", headers=headers)
        soup = BeautifulSoup(req.text, "html.parser")  # html 문서 파싱
        class_pattern = re.compile("nclicks\(itn")
        newses = soup.findAll("a", class_=class_pattern)  # 헤드라인 뉴스 제목의 태그와 class 속성 값
        for i, news in enumerate(newses):
            news_info = []
            news_info.append(news.text)
            news_info.append(news["href"])
            news_infos.append(news_info)

        if (i * len(newses)) % save_every == 0:
            news_infos = save_csv(
                news_infos, check_start, (i * len(newses)), save_path, kst
            )
            check_start = i * len(newses)

        if delay:
            time.sleep(delay)
    save_csv(news_infos, check_start, (i * len(newses)), save_path, kst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--delay", default=0, type=int, help="Crawling delay를 설정해 block을 방지합니다."
    )
    parser.add_argument(
        "-s",
        "--save_every",
        default=10000,
        type=int,
        help="뉴스 기사가 csv로 저장되는 개수를 설정합니다.",
    )
    parser.add_argument(
        "--section", default=105, type=int, help="네이버 뉴스 분야별 코드를 입력합니다. sid1=xxx"
    )
    parser.add_argument(
        "--start_iter", default=1, type=int, help="Crawling 시작 페이지를 지정합니다."
    )
    parser.add_argument(
        "--end_iter", default=2, type=int, help="Crawling 종료 페이지를 지정합니다."
    )
    parser.add_argument(
        "--header",
        default="INSERT YOUR CHROME HEADER",
        type=str,
        help="개인 header를 입력합니다. 입력하지 않으면 접속에 오류가 생길 수 있습니다.",
    )
    parser.add_argument(
        "--save_path", default="./navernews/", type=str, help="csv를 저장할 경로를 지정합니다."
    )
    args = parser.parse_args()
    headline_crawler(
        args.delay,
        args.save_every,
        args.section,
        args.start_iter,
        args.end_iter,
        args.header,
        args.save_path,
    )
