from heapq import nsmallest
from math import hypot
from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    return nsmallest(k, points, key=lambda p: hypot(*p))
