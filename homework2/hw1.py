"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """The function returns 10 longest words consisting of largest number of unique symbols"""
    words_stats = {}
    with open(file_path) as fi:
        words = [
            word.encode("utf-8").decode("unicode-escape")
            for line in fi
            for word in line.split()
        ]
        for i in words:
            words_stats[i] = len(set(i.lower()))
    most_popular = sorted(words_stats.items(), key=lambda x: x[1], reverse=True)[:10]
    return [x[0] for x in most_popular]


def get_rarest_char(file_path: str) -> str:
    """The function returns the rarest symbol for the document"""
    words_stats = {}
    with open(file_path) as fi:
        words = [
            word.encode("utf-8").decode("unicode-escape")
            for line in fi
            for word in line.split()
        ]
        for i in words:
            if i not in words_stats:
                words_stats[i] = 1
            else:
                words_stats[i] += 1
    return sorted(words_stats.items(), key=lambda x: x[1])[:1][0][0]


def count_punctuation_chars(file_path: str) -> int:
    """The function counts every punctuation char"""
    punctuation = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    with open(file_path) as fi:
        c = "".join(fi.readlines())
    c = c.encode("utf-8").decode("unicode-escape")
    return len([x for x in c if x in punctuation])


def count_non_ascii_chars(file_path: str) -> int:
    """The function counts every non ascii char"""
    with open(file_path) as fi:
        c = "".join(fi.readlines())
    c = c.encode("utf-8").decode("unicode-escape")
    return len([x for x in c if ord(x) > 127])


def get_most_common_non_ascii_char(file_path: str) -> str:
    """The function returns the most common non ascii char for the document"""
    with open(file_path, encoding="utf-8") as fi:
        c = "".join(fi.readlines())
    c = c.encode("utf-8").decode("unicode-escape")
    words_stats = {}
    for i in c:
        if ord(i) > 127:
            if i not in words_stats:
                words_stats[i] = 1
            else:
                words_stats[i] += 1
    return sorted(words_stats.items(), key=lambda x: x[1], reverse=True)[:1][0][0]
