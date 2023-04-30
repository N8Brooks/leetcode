from typing import List


def can_partition(nums: List[int]) -> bool:
    q, r = divmod(sum(nums), 2)
    if r:
        return False
    memo = 1 << q
    for num in nums:
        memo |= memo >> num
    return bool(memo & 1)


def test_example_1() -> None:
    assert can_partition([1, 5, 11, 5]) is True


def test_example_2() -> None:
    assert can_partition([1, 2, 3, 5]) is False


def test_small() -> None:
    assert can_partition([1, 2, 5]) is False
