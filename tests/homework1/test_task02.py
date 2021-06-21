import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    "sequence, expected_result", [([1, 1, 1, 2], False), ([0, 0, 0], False)]
)
def test_invalid_sequences(sequence, expected_result):
    """Testing that an invalid sequence returns False"""
    assert check_fibonacci(sequence) == expected_result


@pytest.mark.parametrize(
    "sequence, expected_result", [([1, 1, 1, 2], False), ([0, 0, 0], False)]
)
def test_invalid_sequences(sequence, expected_result):
    """Testing that an invalid sequence returns False"""
    assert check_fibonacci(sequence) == expected_result


def test_empty_case():
    """Testing that empty sequence returns False"""
    assert not check_fibonacci([])
