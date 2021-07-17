import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    "sequences, expected_result",
    [
        (([2, -2], [1, 0], [0, 1], [0, 0]), 2),
        (([0, -2], [-2, 0], [2, 1], [0, 1]), 4),
        (([2, 2], [0, -1], [0, -2], [-1, -2]), 4),
        (([-1, -2], [1, 2], [-1, -1], [2, 1]), 6),
    ],
)
def test_valid_sequences(sequences, expected_result):
    """Testing that the function returns a correct result
     with non empty lists"""
    assert check_sum_of_four(*sequences) == expected_result


def test_empty_lists_case():
    """Testing that function returns a correct result
    with empty lists"""
    assert check_sum_of_four([], [], [], []) == 0
