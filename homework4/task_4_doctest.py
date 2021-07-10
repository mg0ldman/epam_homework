"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Function that takes a number N and returns N FizzBuzz numbers

    >>> fizzbuzz(15)
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz',
    11, 'fizz', 13, 14, 'fizzbuzz']
    >>> fizzbuzz(0)
    []
    >>> fizzbuzz(-1)
    Traceback (most recent call last):
    ...
    ValueError: "n" argument should be a positive number!
    >>> fizzbuzz('a')
    Traceback (most recent call last):
    ...
    TypeError: "n" argument should be an integer!

    """
    if not isinstance(n, int):
        raise TypeError('"n" argument should be an integer!')
    if n < 0:
        raise ValueError('"n" argument should be a positive number!')

    return ['fizzbuzz' if i % 5 == 0 and i % 3 == 0 else 'fizz' if i % 3 == 0
            else 'buzz' if i % 5 == 0 else i for i in range(1, n+1)]
