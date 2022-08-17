from math import inf
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    heights.append(-inf)
    stack = [-1]
    max_area = 0
    for k, height in enumerate(heights):
        i = k
        while height < heights[stack[-1]]:
            j = stack.pop()
            area = (k - j) * heights[j]
            max_area = max(max_area, area)
            i = j
        if height != heights[stack[-1]]:
            stack.append(i)
            heights[i] = height
    return max_area
