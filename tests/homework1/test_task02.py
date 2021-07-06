import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    "sequence, expected_result", [([0, 1, 1, 2, 3, 5, 8, 13], True),
                                  ([233, 377, 610, 987, 1597, 2584], True)]
)
def test_valid_sequences(sequence, expected_result):
    """Testing that a valid sequence returns True"""
    assert check_fibonacci(sequence) == expected_result


@pytest.mark.parametrize(
    "sequence, expected_result", [([1, 1, 1, 2], False), ([0, 0, 0], False)]
)
def test_invalid_sequences(sequence, expected_result):
    """Testing that an invalid sequence returns False"""
    assert check_fibonacci(sequence) == expected_result


def test_empty_case():
    """Testing that an empty sequence returns False"""
    assert not check_fibonacci([])
