import argparse
import pandas as pd
from tqdm import tqdm
import os
import time
import pytz
import datetime
from selenium import webdriver


def save_csv(news_infos, check_start, check_end, save_path, kst):
    print(f"..저장하는 뉴스의 개수: {len(news_infos)}..")
    print(f"..저장하는 뉴스의 번호: {check_start}-{check_end - 1}..")
    now = datetime.datetime.now(kst)
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    df = pd.DataFrame(news_infos, columns=["title", "url"])
    df.to_csv(
        os.path.join(
            save_path,
            f"headline_{check_start}-{check_end - 1}_{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}.csv",
        ),
        index=False,
    )
    print(
        f"저장 완료! 'headline_{check_start}-{check_end - 1}_{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}.csv'"
    )
    return list()


def headline_crawler(
    delay, save_every, section, start_page, end_page, driver_path, save_path
):
    kst = pytz.timezone("Asia/Seoul")
    driver = webdriver.Chrome(driver_path)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    news_infos = []  # title, link

    base_url = f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={section}#&date=%2000:00:00&page="
    check_start = 0
    cnt = 0
    for i in tqdm(range(start_page, end_page + 1)):
        url = f"{base_url}{i}"  # set page
        driver.get(url)
        driver.refresh()  # to avoid error that element is no longer in the DOM, or it changed
        newses = driver.find_elements_by_css_selector('a[class*="airsGParam"]')
        for i, news in enumerate(newses):
            news_info = []
            try:
                if news.text:  # Nan pass
                    news_info.append(news.text)
                    news_info.append(news.get_attribute("href"))
                    news_infos.append(news_info)
                    cnt += 1
            except:
                pass
            if cnt == save_every:
                news_infos = save_csv(
                    news_infos, check_start, check_start + cnt, save_path, kst
                )
                check_start += cnt
                cnt = 0
        if delay:
            time.sleep(delay)
    save_csv(news_infos, check_start, check_start + cnt, save_path, kst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--delay", default=0, type=int, help="Crawling delay를 설정해 block을 방지합니다."
    )
    parser.add_argument(
        "-s",
        "--save_every",
        default=500,
        type=int,
        help="뉴스 기사가 csv로 저장되는 개수를 설정합니다.",
    )
    parser.add_argument(
        "--section", default=105, type=int, help="네이버 뉴스 분야별 코드를 입력합니다. sid1=xxx"
    )
    parser.add_argument(
        "--start_page", default=1, type=int, help="Crawling 시작 페이지를 지정합니다."
    )
    parser.add_argument(
        "--end_page", default=70, type=int, help="Crawling 종료 페이지를 지정합니다."
    )
    parser.add_argument(
        "-dp",
        "--driver_path",
        default="C:/Users/PC/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe",
        type=str,
        help="Chrome driver가 저장된 경로를 입력합니다.",
    )
    parser.add_argument(
        "--save_path", default="./navernews/", type=str, help="csv를 저장할 경로를 지정합니다."
    )
    args = parser.parse_args()
    headline_crawler(
        args.delay,
        args.save_every,
        args.section,
        args.start_page,
        args.end_page,
        args.driver_path,
        args.save_path,
    )
