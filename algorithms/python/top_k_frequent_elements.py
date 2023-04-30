from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    return [num for num, _ in Counter(nums).most_common(k)]


def test_example_1():
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_example_2():
    assert top_k_frequent([1], 1) == [1]
