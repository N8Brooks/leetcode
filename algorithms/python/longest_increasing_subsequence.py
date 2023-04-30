from bisect import bisect_left
from math import inf
from typing import List


def length_of_lis(nums: List[int]) -> int:
    subsequence = [-inf]
    for num in nums:
        if num > subsequence[-1]:
            subsequence.append(num)
        else:
            i = bisect_left(subsequence, num)
            subsequence[i] = num
    return len(subsequence) - 1


def test_example_1():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_example_2():
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4


def test_example_3():
    assert length_of_lis([7, 7, 7, 7, 7, 7, 7]) == 1


def test_negative():
    assert length_of_lis([-2, -1]) == 2
