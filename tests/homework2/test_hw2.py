import pytest

from homework2.hw2 import major_and_minor_elem


@pytest.mark.parametrize(
    "sequence, expected_result",
    [(([3, 2, 3]), (3, 2)), (([2, 2, 1, 1, 1, 2, 2]), (2, 1))],
)
def test_valid_sequences(sequence, expected_result):
    """Testing that the function returns correct results with some sample data"""
    assert major_and_minor_elem(sequence) == expected_result


def test_empty_lists_case():
    """Testing that function returns a correct result
    with an empty list"""
    assert major_and_minor_elem([]) is None
