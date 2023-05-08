from bisect import bisect_right
from typing import Iterable, List


def k_increasing(arr: List[int], k: int) -> int:
    return len(arr) - sum(
        n_non_decreasing(arr[j] for j in range(i, len(arr), k)) for i in range(k)
    )


def n_non_decreasing(nums: Iterable[int]) -> int:
    stack: List[int] = []
    for num in nums:
        if stack and stack[-1] > num:
            i = bisect_right(stack, num)
            stack[i] = num
        else:
            stack.append(num)
    return len(stack)


def test_example_1():
    assert k_increasing([5, 4, 3, 2, 1], 1) == 4


def test_example_2():
    assert k_increasing([4, 1, 5, 2, 6, 2], 2) == 0


def test_example_3():
    assert k_increasing([4, 1, 5, 2, 6, 2], 3) == 2


def test_example_duplicates():
    assert k_increasing([2, 2, 2, 2, 2, 1, 1, 4, 4, 3, 3, 3, 3, 3], 1) == 4
