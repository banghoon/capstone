from krwordrank.word import KRWordRank
from eunjeon import Mecab
import re
import pandas as pd


# f = open('korean_stopwords.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# stopword_list = ['있다', '있는', '통해', '것으로', '대한', '너무', '진짜', '아니고', '위해', '한다', '먼저', '다음으로', '예를', '들면',
#              '이때', '하다', '이번', '대해', '모드', '누구', '라며', '만큼', '부분', '여러', '각각', '당시', '더욱', '다만', '반면',
#              '면서', '로서', '지난', '여기', '거의', '그동안', '우선', '바로', '거나', '로부터', '하고', '직접', '했다', '여전히',
#              '기자']
# for line in lines:
#     line = line.replace('\n', '')
#     stopword_list.append(line)
# f.close()

'''
min_count=5
max_length=10
beta = 0.85
max_iter = 10
'''


def keyword(data, min_count=5, max_length=10, beta=0.85, max_iter=20, keyword_num=2000, stopwords=None):
    keywords_extractor = KRWordRank(min_count=min_count, max_length=max_length, verbose=True)
    keywords, rank, graph = keywords_extractor.extract(data, beta, max_iter)
    if stopwords:
        today_keywords = [word for word, _ in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:keyword_num]
                          if not (word in stopwords)]
    else:
        today_keywords = [word for word, _ in sorted(keywords.items(), key=lambda x: x[1], reverse=True)][:keyword_num]
    return today_keywords, keywords


def keyword_extrator(data, rank, top=10, today_keywords=None):
    res = {}
    for d in data.split():
        if d in today_keywords:
           res[d] = rank[d]
    res = sorted(res.items(), key=lambda x: -x[1])[:top]


    return ' '.join(["#"+i[0] for i in res])



def preprocessing(reviews):
    tagger = Mecab()
    total_review = ''
    for review in reviews:
        sentence = str(review)
        sentence = re.sub('\n', ' ', sentence)
        sentence = re.sub('\u200b', ' ', sentence)
        sentence = re.sub('\xa0', ' ', sentence)
        sentence = re.sub('([a-zA-Z])', ' ', sentence)
        sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', ' ', sentence)
        sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', sentence)
        if len(sentence) == 0:
            continue
        sentence = tagger.pos(sentence)
        word = []
        for i in sentence:
            if not i[1] in ['NNG', 'NNP']:  #명사가 아니면
                continue
            if len(i[0]) == 1:  #글자길이가 1
                continue
            word.append(i[0])
        word = ' '.join(word)
        word += '. '
        total_review += word
    return total_review