from itertools import chain, combinations
from typing import Generator, List, Tuple


def powerset(nums: List[int]) -> Generator[Tuple[int], None, None]:
    """Defined in itertools documentation recipes"""
    yield from chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))


def subsets(nums: List[int]) -> List[List[int]]:
    return [list(combination) for combination in powerset(nums)]
