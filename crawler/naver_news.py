from selenium import webdriver
import numpy as np
import pandas as pd
from selenium.webdriver.common.keys import Keys
from eunjeon import Mecab
import re
import warnings


warnings.simplefilter('ignore')


def tokenizer(news, morph):  # news : 크롤링 기사 1개 / morph : 원하는 품사 리스트
    news = re.sub('[^가-힣a-zA-Z0-9]', ' ', news)
    tagger = Mecab()
    tag = tagger.pos(news)
    news = [t[0] for t in tag if (t[1] in morph) & (len(t[0]) != 1)]
    news = ' '.join(news)
    news += ". "
    return news


def find_last_page(url, path='C:/Users/bhkim/PycharmProjects/capstone/crawler/chromedriver/chromedriver_95.exe'):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(path, options=options)
    driver.get(url + '&page=10000')
    result = driver.find_element_by_xpath('//*[@id="main_content"]/div[3]/strong')
    last_page = result.text
    driver.close()
    return last_page


def crawling_news(date, path='C:/Users/bhkim/PycharmProjects/capstone/crawler/chromedriver/chromedriver_95.exe'):
    menu = {
        '100': '정치', '101': '경제', '102': '사회', '103': '생활/문화', '104': '세계', '105': 'IT/과학'
    }
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("--mute-audio")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(path, options=options)
    datalist = []
    for path in [str(i) for i in range(100, 106)]:
        url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&date={str(date)}&sid1={str(path)}'
        pages = int(find_last_page(url))
        for page in range(pages):
            print(f'-------------------{page+1}/{pages}-------------------')
            driver.get(url + f'&page={page+1}')

            for i in [1, 2]:
                results = driver.find_elements_by_xpath(
                    f'//div[@id="main_content"]/div/ul[{i}]/li/dl/dt/a[@class="nclicks(fls.list)"]')
                comps = driver.find_elements_by_xpath('//div[@id="main_content"]/div/ul/li/dl/dd/span[2]')

                for comp, result in zip(comps, results):
                    if (result.text == '동영상기사') or (result.text == ''):
                        continue
                    result.send_keys(Keys.CONTROL + "\n")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.implicitly_wait(20)
                    try:
                        url_res = driver.find_element_by_xpath('//div[@id="articleBodyContents"]')
                        res = url_res.text.replace('\n', '')

                    except:
                        try:
                            url_res = driver.find_element_by_xpath('//div[@id="newsEndContents"]')
                            res = url_res.text.replace('\n', '')

                        except:
                            res = " "

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    driver.implicitly_wait(20)
                    datalist.append({
                        'date': date,
                        'category': menu[path],
                        'title': result.text,
                        'company': comp.text,
                        'url': result.get_attribute("href"),
                        'text': str(res),
                        'tokenize': tokenizer(str(res), ['NNG', 'NNP']),
                        # 'summary': summarize.get_summary(result.text, "./summary/kobart_summary")
                    })
    # pd.DataFrame(datalist).to_csv(f'C:/Users/bhkim/PycharmProjects/capstone/data/news_{date}.csv', encoding='utf-8-sig')
    print('-------------------END-------------------')
    driver.quit()
    return pd.DataFrame(datalist)


if __name__ == '__main__':
    crawling_news("20211030")

