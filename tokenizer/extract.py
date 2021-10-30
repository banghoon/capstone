from krwordrank.word import KRWordRank


def keyword(data, min_count, max_length, beta, max_iter, keyword_num=1000, stopwords=None):
    keywords_extractor = KRWordRank(min_count=min_count, max_length=max_length, verbose=True)
    keywords, rank, graph = keywords_extractor.extract(data, beta, max_iter)
    if stopwords:
        today_keywords = [word for word, _ in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:keyword_num]
                    if not (word in stopwords)]
    else:
        today_keywords = [word for word, _ in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:keyword_num]]
    return today_keywords


def keyword_v2(data, min_count, max_length, beta, max_iter, keyword_num=1000, today_keywords=None):
    keywords_extractor = KRWordRank(min_count=min_count, max_length=max_length, verbose=True)
    keywords, rank, graph = keywords_extractor.extract(data, beta, max_iter)
    if today_keywords:
        keywords = [word for word, _ in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:keyword_num]
                    if word in today_keywords]
    else:
        keywords = [word for word, _ in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:keyword_num]]
    return keywords
