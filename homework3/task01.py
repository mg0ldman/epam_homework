"""In previous homework task 4, you wrote a cache function
that remembers other function output value."""
from typing import Callable


def cache(times: int) -> Callable:
    """The function returns a cached result of the argument-function
     for a given number of times"""
    cache_storage = []
    cnt = 0
    if times < 0:
        raise ValueError('"times" argument should be greater '
                         'than or equal to zero')

    def wrapper(func):
        def cached_func(*args, **kwargs):
            nonlocal cnt
            if cnt == 0:
                cache_storage.clear()
                cnt += 1
                cache_storage.append((func, func(*args, **kwargs)))
            if times >= cnt > 0:
                cnt += 1
            else:
                cnt = 0
            return cache_storage[0]
        return cached_func
    return wrapper
