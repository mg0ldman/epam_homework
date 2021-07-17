"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """The function returns a sum of a sub-array with length less or equal to "k"
    , with maximal sum"""
    if not nums:
        return 0
    max_sum = nums[0]
    for i in range(len(nums)):
        for j in range(k):
            if sum(nums[i: i + k][j:]) > max_sum:
                max_sum = sum(nums[i: i + k][j:])
    return max_sum
