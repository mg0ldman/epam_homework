"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    """The function caches result of the argument-function"""
    cache_storage = {}

    def cached_func(*args):
        if args in cache_storage:
            return cache_storage[args]
        else:
            cache_storage[args] = func(*args)
        return cache_storage[args]

    return cached_func
