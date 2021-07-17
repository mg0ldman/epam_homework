from homework1.task05 import find_maximal_subarray_sum


def test_non_empty_list_case():
    """Testing that the function returns a correct result
    with a nonempty list"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_empty_list_case():
    """Testing that function returns a correct result
    when list's length is zero"""
    assert find_maximal_subarray_sum([], 0) == 0
