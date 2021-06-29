from homework2.hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_sample_data_longest_diverse_words():
    """Testing that the function returns a correct result
    with a list of 10 longest words based on the data from a sample file"""
    assert get_longest_diverse_words("data.txt") == [
        "unmißverständliche",
        "Bevölkerungsabschub,",
        "Kollektivschuldiger,",
        "résistance-Bewegungen,",
        "Werkstättenlandschaft",
        "Schicksalsfiguren;",
        "Machtbewußtsein,",
        "politisch-strategischen",
        "Zwingherrschaft.",
        "Zahlenverhältnis-",
    ]


def test_sample_data_rarest_char():
    """Testing that the function returns a correct result
    with a least popular symbol based on the data from a sample file"""
    assert get_rarest_char("data.txt") == "S"


def test_sample_data_punctuation_chars():
    """Testing that the function returns a correct result
    with a punctuation chars count based on the data from a sample file"""
    assert count_punctuation_chars("data.txt") == 5305


def test_sample_data_non_ascii_chars():
    """Testing that the function returns a correct result
    with a non ascii chars count based on the data from a sample file"""
    assert count_non_ascii_chars("data.txt") == 2972


def test_sample_data_most_common_non_ascii_char():
    """Testing that the function returns a correct result
    with a non ascii chars count based on the data from a sample file"""
    assert get_most_common_non_ascii_char("data.txt") == "ä"
