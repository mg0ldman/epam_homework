"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import unicodedata


def get_longest_diverse_words(file_path: str) -> List[str]:
    """The function returns 10 longest words
    consisting of largest number of unique symbols"""
    words_stats = {}
    file = open(file_path, encoding='unicode-escape')
    for line in file:
        for i in line.split():
            words_stats[i] = len(set(i.lower()))
    most_popular = sorted(words_stats.items(), key=lambda x: x[1],
                          reverse=True)[:10]
    return [x[0] for x in most_popular]


def get_rarest_char(file_path: str) -> str:
    """The function returns the rarest symbol for the document"""
    words_stats = {}
    file = open(file_path, encoding='unicode-escape')
    for line in file:
        for i in line:
            if i not in words_stats:
                words_stats[i] = 1
            else:
                words_stats[i] += 1
    return sorted(words_stats.items(), key=lambda x: x[1])[:1][0][0]


def count_punctuation_chars(file_path: str) -> int:
    """The function counts every punctuation char"""
    cnt = 0
    file = open(file_path, encoding='unicode-escape')
    for line in file:
        for i in line:
            if unicodedata.category(i)[0] == 'P':
                cnt += 1
    return cnt


def count_non_ascii_chars(file_path: str) -> int:
    """The function counts every non ascii char"""
    cnt = 0
    file = open(file_path, encoding='unicode-escape')
    for line in file:
        for i in line:
            if ord(i) > 127:
                cnt += 1
    return cnt


def get_most_common_non_ascii_char(file_path: str) -> str:
    """The function returns the most common non ascii char for the document"""
    words_stats = {}
    file = open(file_path, encoding='unicode-escape')
    for line in file:
        for i in line:
            if ord(i) > 127:
                if i not in words_stats:
                    words_stats[i] = 1
                else:
                    words_stats[i] += 1
    return sorted(words_stats.items(), key=lambda x: x[1],
                  reverse=True)[:1][0][0]
