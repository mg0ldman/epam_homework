"""
Armstrong number is a number that is the sum of
its own digits each raised to the power of the number of digits.
"""


def is_armstrong(number: int) -> bool:
    """Checks if a number is an Armstrong one"""
    if number < 0:
        raise ValueError('a "number" argument should be a natural number')
    number = str(number)
    return sum([x**len(number) for x in map(int, number)]) == int(number)
