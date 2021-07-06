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


def create_custom_range(seq, *args):
    """The function accepts any iterable of unique values and
    then it behaves as a range function"""
    def parse_args(*args):
        k = len(args)
        start = None
        step = 1
        if k == 1:
            stop = args[0]
        if k == 2:
            start = args[0]
            stop = args[1]
        if k == 3:
            start = args[0]
            stop = args[1]
            step = args[-1]
        return start, stop, step
    start, stop, step = parse_args(*args)
    if not start:
        return list(seq[:seq.index(stop):step])
    return list(seq[seq.index(start):seq.index(stop):step])
