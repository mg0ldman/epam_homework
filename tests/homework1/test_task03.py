import pytest

from homework1.task03 import find_maximum_and_minimum


def test_with_predefined_numbers():
    """Testing if the function returns a correct result with the data read from a sample file"""
    assert 1, 100 == find_maximum_and_minimum("some_file.txt")
