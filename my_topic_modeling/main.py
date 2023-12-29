import typing as t
import numpy as np
import os

from collections import defaultdict

import re

from logger import logger
from sparse_matrix import SparseMatrix


# 1. Remove stopwords
# 2. Lower case data -- for increased normalization
# 3. Remove high frequency words
# 4. Bag-Of-Words
# 5. LDA
# needs 3 inputs: 
# - document-term matrix
# - number of topics in documents 
# - number of iterations - get optimal words-per-topic combinations
# 5.1 

STOPWORDS = "data/english_stopwords.txt"
DIR_NEWS = "data/20news-18828"


def get_stopwords() -> t.List:
    with open(STOPWORDS, "r") as f:
        return [line[:-1] for line in f.readlines()]


def get_news() -> t.Dict:
    all_news = defaultdict(lambda: [])
    for news_type in os.listdir(DIR_NEWS):
        for filename in os.listdir(f"{DIR_NEWS}/{news_type}"):
            with open(f"{DIR_NEWS}/{news_type}/{filename}", "rb") as f:
                read_news = f.read()
                try:
                    news = read_news.decode("windows-1254")
                except UnicodeDecodeError:
                    logger.info("Error with the following text")
                    logger.error(read_news)
                    raise
                all_news[news_type].append(news)
    return all_news


def remove_stopwords(text: str, stopwords: t.List[str]) -> str:
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    text = re.sub(' +', ' ', text)
    text = text.lower().strip()
    return ' '.join(set(text.split(' ')) - set(stopwords))


def bag_of_words(documents: t.Iterable[t.List[str]]):
    """
    documents: t.Iterable[t.List[str]]

    get dictionary with word_id
    matrix of values
    """
    word_id = {}
    all_words = defaultdict(lambda: 0)

    words_count = 0
    for document in documents:
        for word in document:
            if word not in word_id:
                word_id[word] = words_count
                words_count += 1
            all_words[word_id[word]] += 1
    documents_vectors = SparseMatrix()

    return word_id, all_words, documents_vectors




if __name__ == "__main__":

    logger.info("Getting stopwords")
    stop_words = get_stopwords()
    news = get_news()

    logger.debug("Remove stopwords and short words")
    documents = []
    document_newstype = {}
    for i, news_type in enumerate(news):
        documents.extend([
            remove_stopwords(text, stop_words).split(" ")
            for text in news[news_type]
            if len(text) > 2
        ])
        document_newstype[i] = news_type

    word_id, all_words, document_vectors = bag_of_words(documents)

