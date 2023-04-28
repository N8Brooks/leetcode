from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    lo, hi = intervals[0]
    result = []
    for a, b in intervals:
        if a > hi:
            result.append([lo, hi])
            lo = a
            hi = b
        else:
            hi = max(hi, b)
    result.append([lo, hi])
    return result
