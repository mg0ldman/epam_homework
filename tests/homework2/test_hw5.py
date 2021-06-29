import string

import pytest

from homework2.hw5 import create_custom_range


@pytest.mark.parametrize(
    "args, expected_result",
    [
        ((string.ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        (
            (string.ascii_lowercase, "g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ((string.ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
    ],
)
def test_valid_sequences(args, expected_result):
    """Testing that the function returns correct results with some sample data"""
    assert create_custom_range(*args) == expected_result
