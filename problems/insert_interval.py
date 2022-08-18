import bisect
from math import inf
from typing import List

# fmt: off

def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    i = bisect.bisect_left(intervals, True, key=lambda interval: interval[1] >= new_interval[0])
    j = bisect.bisect_left(intervals, [new_interval[1], inf], lo=i)
    left = (min(intervals[i][0], new_interval[0]) if i < len(intervals) else new_interval[0])
    right = max(intervals[j - 1][1], new_interval[1]) if j > 0 else new_interval[1]
    intervals[i:j] = [[left, right]]
    return intervals
