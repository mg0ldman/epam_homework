import pytest

from homework3.task04 import is_armstrong


@pytest.mark.parametrize(
    "number, expected_result", [(3, True),
                                (153, True),
                                (8208, True),
                                (548834, True)]
)
def test_is_armstrong_positive(number, expected_result):
    """Testing that a valid number returns True"""
    assert is_armstrong(number) == expected_result


def test_is_armstrong_negative():
    pytest.raises(ValueError, is_armstrong, -2)


def test_is_armstrong_zero():
    assert is_armstrong(0) is True
