from itertools import chain
from math import inf
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    heights.append(-inf)  # type: ignore
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


def test_example_1() -> None:
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10


def test_example_2() -> None:
    assert largest_rectangle_area([2, 4]) == 4


def test_zero() -> None:
    assert largest_rectangle_area([0]) == 0


def test_one() -> None:
    assert largest_rectangle_area([1]) == 1


def test_two() -> None:
    assert largest_rectangle_area([2]) == 2


def test_many_ones() -> None:
    assert largest_rectangle_area([1] * 30_000) == 30_000


def test_two_one_two() -> None:
    assert largest_rectangle_area([2, 1, 2]) == 3


def test_large() -> None:
    heights = list(chain.from_iterable(10 * [i] for i in range(10_000)))
    assert largest_rectangle_area(heights) == 250_000_000


def test_four_two() -> None:
    assert largest_rectangle_area([4, 2]) == 4


def test_large_range() -> None:
    assert largest_rectangle_area(list(range(24_000))) == 144_000_000


def test_snake_eyes() -> None:
    assert largest_rectangle_area([1, 1]) == 2
