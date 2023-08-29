import requests
from bs4 import BeautifulSoup
import argparse
import pandas as pd
import time
from tqdm import tqdm
import os
from selenium import webdriver
from bs4 import BeautifulSoup


def only_csv(file_list, path):
    csvs = []
    for file_name in file_list:
        if file_name.endswith(".csv"):
            file_path = os.path.join(path, file_name)
            csv_data = pd.read_csv(file_path)
            csvs.append([csv_data, file_name])
    return csvs


def drop_duplicated_csv(csv_list):
    print("..중복된 기사 drop..")
    csv_cleaned = []
    csv_names = []
    print("csv의 개수:", len(csv_list))
    for csv in csv_list:
        csv_cleaned.append(csv[0].drop_duplicates())
        csv_names.append(csv[1])
    for i in range(len(csv_names)):
        print(f"{csv_names[i]}: {len(csv_list[i][0])} -> {len(csv_cleaned[i])}")
    print("headline csv의 날짜와 시각이 summary csv의 이름에도 적용됩니다.")
    return csv_cleaned, csv_names


def save_csv(all_news, id, save_path, csv_names):
    date = csv_names[id].split("_")
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    df = pd.DataFrame(all_news, columns=["body", "summary"])
    print(f"..저장하는 뉴스의 개수: {len(df)}.. ")
    df.to_csv(os.path.join(save_path, f"summary_{date[-2]}_{date[-1]}"), index=False)
    print(f"저장 완료! 'summary_{date[-2]}_{date[-1]}'")


def load_url(csv_path):
    file_list = os.listdir(csv_path)
    csv_list = only_csv(file_list, csv_path)
    csv_list, csv_names = drop_duplicated_csv(csv_list)
    url_list = []
    for csv in csv_list:
        url_list.append(csv["url"])
    return url_list, csv_names


def news_crawler(delay, sleep_delay, csv_path, driver_path, save_path):
    driver = webdriver.Chrome(driver_path)
    csv_urls, csv_names = load_url(csv_path)
    print("..크롤링 시작..")
    for id, urls in enumerate(csv_urls):
        print(csv_names[id])
        news_texts = []
        for url in tqdm(urls):
            try:
                bodyandsummary = []
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, "html.parser")
                # <article> 태그 내의 텍스트 추출
                article = soup.find("article", class_="go_trans _article_content")
                for br in article.find_all("br"):
                    br.replace_with("\n")
                article_text = article.get_text()

                # <article> 태그 내의 내용 중 <em> 태그(주석) 제외
                exclude_em = article.find_all("em")
                for em_tag in exclude_em:
                    article_text = article_text.replace(em_tag.get_text(), " ")

                # <article> 태그 내의 내용 중 <strong> 태그(강조 반복) 제외
                exclude_strong = article.find_all("strong")
                for strong_tag in exclude_strong:
                    article_text = article_text.replace(strong_tag.get_text(), " ")
                bodyandsummary.append(article_text)

                driver.find_element_by_xpath('//*[@id="_SUMMARY_BUTTON"]/a').click()
                time.sleep(sleep_delay)
                news = driver.find_element_by_css_selector(
                    "div._contents_body._SUMMARY_CONTENT_BODY"
                )
                bodyandsummary.append(news.text)
                news_texts.append(bodyandsummary)
            except:
                pass

            if delay:
                time.sleep(delay)

        save_csv(news_texts, id, save_path, csv_names)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--delay", default=0, type=int, help="Crawling delay를 설정해 block을 방지합니다."
    )
    parser.add_argument(
        "-cp",
        "--csv_path",
        default="./navernews/",
        type=str,
        help="csv가 저장된 path를 입력합니다.",
    )
    parser.add_argument(
        "-dp",
        "--driver_path",
        default="C:/Users/PC/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe",
        type=str,
        help="Chrome driver가 저장된 경로를 입력합니다.",
    )
    parser.add_argument(
        "-s",
        "--sleep_delay",
        default=1,
        type=int,
        help="버튼을 누르고 대기할 시간을 입력합니다. 너무 짧으면 추출되지 않을 수 있습니다.",
    )
    parser.add_argument(
        "-sp",
        "--save_path",
        default="./navernews/text",
        type=str,
        help="저장할 경로를 지정합니다.",
    )
    args = parser.parse_args()
    news_crawler(
        args.delay, args.sleep_delay, args.csv_path, args.driver_path, args.save_path
    )
