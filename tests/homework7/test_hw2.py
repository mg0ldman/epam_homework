import pytest

from homework7.hw2 import compare_backspace


@pytest.mark.parametrize(
    "strings, expected_result", [(("ab#c", "ad#c"), True),
                                 (("a##c", "#a#c"), True),
                                 (("caa###", "d#a#b#"), True)]
)
def test_compare_backspace_positive(strings, expected_result):
    """Testing that function returns True if the strings match
    when both are typed into empty text editors"""
    assert compare_backspace(*strings) is expected_result


@pytest.mark.parametrize(
    "strings, expected_result", [(("cab#c", "la#d#c"), False),
                                 (("ma#c", "q#a#c"), False),
                                 (("a#c", "b"), False),
                                 (("", "b"), False)]
)
def test_compare_backspace_negative(strings, expected_result):
    """Testing that function returns False if the strings differ
        when both are typed into empty text editors"""
    assert compare_backspace(*strings) is expected_result


def test_compare_backspace_empty_lists():
    """Testing that function returns True if both strings are empty"""
    assert compare_backspace('', '') is True
