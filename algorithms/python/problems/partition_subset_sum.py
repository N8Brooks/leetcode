from typing import List


def can_partition(nums: List[int]) -> bool:
    q, r = divmod(sum(nums), 2)
    if r:
        return False
    memo = 1 << q
    for num in nums:
        memo |= memo >> num
    return bool(memo & 1)
