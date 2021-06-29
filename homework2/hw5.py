"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g')
== ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p')
== ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2)
== ['p', 'n', 'l', 'j', 'h']
"""


def create_custom_range(*args):
    """The function accepts any iterable of unique values and
    then it behaves as a range function"""
    k = len(args)
    if k < 1:
        raise TypeError("custom range expected 1 argument, got 0")
    if k == 2:
        result = args[0][: args[0].index(args[1])]
    elif k == 3:
        result = args[0][args[0].index(args[1]) : args[0].index(args[2])]
    elif k == 4:
        result = args[0][args[0].index(args[1]) : args[0].index(args[2]) : args[-1]]
    return list(map(str, result))
