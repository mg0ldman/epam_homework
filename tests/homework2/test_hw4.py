import pytest

from homework2.hw4 import cache


def test_sample_data_rarest_char():
    """Testing that the function caches result of the argument-function"""
    cache_func = cache(pow)
    val_1 = cache_func(2, 3)
    val_2 = cache_func(2, 3)
    assert val_1 is val_2
