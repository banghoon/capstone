from crawler.naver_news import crawling_news
from summary import summarize
import pandas as pd
from extracter import extract
import warnings


warnings.simplefilter('ignore')


date = "20211104"
result = crawling_news(date)
texts = result.text.to_list()
today_keyword = extract.keyword(extract.preprocessing(texts))
keywords = []
for text in texts:
    keywords.append(extract.keyword_extrator(text, rank=10, today_keywords=today_keyword))
result = pd.concat([result, pd.DataFrame(keywords, columns=['summary'])], axis=1)

res = summarize.get_summary(texts, "./summary/kobart_summary")
pd.concat([result, pd.DataFrame(res, columns=['summary'])], axis=1).to_csv('res.csv', encoding='utf-8-sig')

print('END')