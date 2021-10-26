from crawler.naver_news import crawling_news
from summary import summarize
import pandas as pd


date = "20211026"
cral = crawling_news(date, path='./crawler/chromedriver_94.exe')
text = cral.text.to_list()
res = summarize.get_summary(text, "./summary/kobart_summary")
pd.concat([cral, pd.DataFrame(res, columns=['summary'])], axis=1).to_csv('res.csv', encoding='utf-8-sig')

print(res)


