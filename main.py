from crawler.naver_news import crawling_news
from summary import summarize
import pandas as pd
from extracter import extract
import warnings


warnings.simplefilter('ignore')


f = open('./crawler/korean_stopwords.txt', 'r', encoding='utf-8')
lines = f.readlines()
stopword_list = ['있다', '있는', '통해', '것으로', '대한', '너무', '진짜', '아니고', '위해', '한다', '먼저', '다음으로', '예를', '들면',
                 '이때', '하다', '이번', '대해', '모드', '누구', '라며', '만큼', '부분', '여러', '각각', '당시', '더욱', '다만', '반면',
                 '면서', '로서', '지난', '여기', '거의', '그동안', '우선', '바로', '거나', '로부터', '하고', '직접', '했다', '여전히',
                 '기자', '동영상']
for line in lines:
    line = line.replace('\n', '')
    stopword_list.append(line)
f.close()

date = "20211104"
result = crawling_news(date)
result.drop_duplicates(subset=['text'], ignore_index=True, inplace=True)
result = result.iloc[:, 1:]

result['text'] = result['text'].apply(str)
texts = result.text.to_list()
today_keyword, rank = extract.keyword(extract.preprocessing(texts).split("."), stopwords=stopword_list)
keywords = []
for text in result.tokenize.tolist():
    keywords.append(extract.keyword_extrator(text, rank=rank, today_keywords=today_keyword))
result = pd.concat([result, pd.DataFrame(keywords, columns=['keyword'])], axis=1)
res = summarize.get_summary(texts, "./summary/kobart_summary")
pd.concat([result, pd.DataFrame(res, columns=['summary'])], axis=1).to_csv('res.csv', encoding='utf-8-sig')
print('END')
