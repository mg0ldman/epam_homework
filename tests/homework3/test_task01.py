import pytest

from homework3.task01 import cache


def test_cache_positive():
    """Testing that the function returns a cached result of the argument-function
     for a given number of times"""
    cnt = 0

    @cache(times=2)
    def f():
        nonlocal cnt
        cnt += 1
        return cnt
    results = [f() for x in range(6)]
    assert results[0] == results[2]


def test_cache_negative():
    """Testing that the ValueError raised if
    'times' parameter is a negative number"""
    with pytest.raises(ValueError):
        cnt = 0

        @cache(times=-2)
        def f():
            nonlocal cnt
            cnt += 1
            return cnt


def test_cache_zero():
    """Testing that the function does not return a
    cached result of the argument-function if times argument is equal zero"""
    cnt = 0

    @cache(times=0)
    def f():
        nonlocal cnt
        cnt += 1
        return cnt
    results = [f() for x in range(2)]
    assert not results[0] == results[1]
