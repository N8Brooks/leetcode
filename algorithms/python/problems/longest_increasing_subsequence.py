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
