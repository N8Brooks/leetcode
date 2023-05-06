from itertools import accumulate, islice
from operator import add, sub
from typing import List


def max_sum_two_no_overlap(nums: List[int], a: int, b: int) -> int:
    return max(
        find_max(nums, a, b),
        find_max(nums, b, a),  # pylint: disable=arguments-out-of-order
    )


def find_max(nums: List[int], a: int, b: int) -> int:
    return max(
        map(
            add,
            accumulate(
                map(sub, islice(accumulate(nums), a, None), accumulate(nums)),
                func=max,
                initial=sum(islice(nums, a)),
            ),
            map(
                sub,
                islice(accumulate(nums), a + b - 1, None),
                islice(accumulate(nums), a - 1, None),
            ),
        )
    )


def test_example_1():
    assert max_sum_two_no_overlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2) == 20


def test_example_2():
    assert max_sum_two_no_overlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2) == 29


def test_example_3():
    assert (
        max_sum_two_no_overlap(
            [2, 1, 5, 6, 0, 9, 5, 0, 3, 8],
            4,
            3,
        )
        == 31
    )


def test_total_len():
    assert max_sum_two_no_overlap([1, 0, 3], 1, 2) == 4


def test_space():
    assert max_sum_two_no_overlap([1, 0, 1], 1, 1) == 2
