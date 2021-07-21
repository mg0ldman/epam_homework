from homework7.hw1 import example_tree, find_occurrences


def test_find_occurrences_positive():
    """Testing that the function returns an expected number of
    element's occurrences with some sample data"""
    assert find_occurrences(example_tree, 'RED') == 6


def test_find_occurrences_zero():
    """Testing that the function returns a zero
    when element is not present in the sample data"""
    assert find_occurrences(example_tree, 'YELLOW') == 0
