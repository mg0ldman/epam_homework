"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def generate_symbol(s):
    """A function-generator that yields symbols if there are no
    backspaces before those"""
    accumulated_backspace = 0
    for symbol in reversed(s):
        if not accumulated_backspace and symbol != '#':
            yield symbol
        elif symbol == '#':
            accumulated_backspace += 1
        if symbol != '#' and accumulated_backspace:
            accumulated_backspace -= 1


def compare_backspace(first: str, second: str):
    """A function return if two strings are equal when both are typed into
    empty text editors"""
    return list(generate_symbol(first)) == list(generate_symbol(second))
