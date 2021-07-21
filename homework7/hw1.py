"""
Given a dictionary (tree), that can contain multiple nested structures.
Write a function, that takes an element and finds the number of its occurrences
in the tree.
The tree can only contain basic structures like:
str, list, tuple, dict, set, int, bool
"""
from collections import abc
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """The function returns the number of occurrences
    of a certain value within a dictionary (tree)"""
    cnt = 0
    for key, value in tree.items():
        if element in tree[key] or tree[key] == element:
            cnt += 1
        else:
            if isinstance(value, dict):
                cnt += find_occurrences(value, element)
            elif isinstance(value, abc.Sequence):
                for el in value:
                    if isinstance(el, dict):
                        cnt += find_occurrences(el, element)
    return cnt


example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}
