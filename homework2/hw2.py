"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """The function returns the most common and the least common elements of an array"""
    if not inp:
        return None
    elements_stats = {}
    for i in inp:
        if i not in elements_stats:
            elements_stats[i] = 1
        else:
            elements_stats[i] += 1
    sorted_elements_stats = sorted(
        elements_stats.items(), key=lambda x: x[1] > len(inp) // 2
    )
    return sorted_elements_stats[-1][0], sorted_elements_stats[0][0]
