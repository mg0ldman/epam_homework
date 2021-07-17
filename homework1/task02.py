"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers, and
returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def generate_fib(start_value):
    """Fibonacci sequence generator"""
    a, b = 0, 1
    while True:
        if a >= start_value:
            yield a
        a, b = b, a+b


def check_fibonacci(data: Sequence[int]) -> bool:
    """The function checks if a given sequence is a Fibonacci one"""
    if len(data) < 3:
        return False
    for values_from_fib, values_from_data in zip(data, generate_fib(data[0])):
        if values_from_fib != values_from_data:
            return False
    return True
