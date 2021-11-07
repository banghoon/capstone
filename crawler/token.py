from eunjeon import Mecab
import re


''' 
< TAGSET >
'EC': '연결 어미', 'EF': '종결 어미', 'EP': '선어말어미', 'ETM': '관형형 전성 어미', 'ETN': '명사형 전성 어미', 'IC': '감탄사',
'JC': '접속 조사', 'JKB': '부사격 조사', 'JKC': '보격 조사', 'JKG': '관형격 조사', 'JKO': '목적격 조사', 'JKQ': '인용격 조사', 
'JKS': '주격 조사', 'JKV': '호격 조사', 'JX': '보조사','MAG': '일반 부사', 'MAJ': '접속 부사', 'MM': '관형사', 'NNB': '의존 명사',
'NNBC': '단위를 나타내는 명사', 'NNG': '일반 명사', 'NNP': '고유 명사', 'NP': '대명사', 'NR': '수사','SC': '구분자 , · / :', 
'SE': '줄임표 …', 'SF': '마침표, 물음표, 느낌표', 'SH': '한자', 'SL': '외국어', 'SN': '숫자', 'SSC': '닫는 괄호 ), ]', 
'SSO': '여는 괄호 (, [', 'SY': '기타 기호','VA': '형용사', 'VCN': '부정 지정사', 'VCP': '긍정 지정사', 'VV': '동사', 
'VX': '보조 용언', 'XPN': '체언 접두사', 'XR': '어근', 'XSA': '형용사 파생 접미사', 'XSN': '명사파생 접미사',
'XSV': '동사 파생 접미사'
'''


def tokenizer(news, morph):  # news : 크롤링 기사 1개 / morph : 원하는 품사 리스트
    # series -> list
    # news = news.tolist()
    # 특수문자 제거
    # title = re.sub('[^가-힣a-zA-Z0-9]', ' ', news[2])
    # text = re.sub('[^가-힣a-zA-Z0-9]', ' ', news[5])
    # title, text 품사별로 토큰화
    # tagger = Mecab()
    # tag = tagger.pos(title)
    # tag2 = tagger.pos(text)
    # 원하는 품사만 추출
    # news[2] = [t[0] for t in tag if t[1] in morph]
    # news[5] = [t[0] for t in tag2 if t[1] in morph]

    news = re.sub('[^가-힣a-zA-Z0-9]', ' ', news)
    tagger = Mecab()
    tag = tagger.pos(news)
    news = [t[0] for t in tag if (t[1] in morph) & (len(t[0]) != 1)]
    news = ' '.join(news)
    news += ". "
    return news


# 뉴스 기사 불러오기
# if __name__ == "__main__":
#     news_data = pd.read_csv('news22to27.csv', encoding="utf-8-sig", index_col=0)
#     news = news_data.text[0]
#     news_1 = tokenizer(news, ['NNG', 'NNP'])
#     # print(news.tolist())
#     print(news_1)



