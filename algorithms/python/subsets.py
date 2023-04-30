from itertools import chain, combinations
from typing import Generator, List, Tuple


def powerset(nums: List[int]) -> Generator[Tuple[int], None, None]:
    """Defined in itertools documentation recipes"""
    yield from chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))


def subsets(nums: List[int]) -> List[List[int]]:
    return [list(combination) for combination in powerset(nums)]


def make_tuple_set(list_of_subsets):
    return set(tuple(subset) for subset in list_of_subsets)


def test_example_1() -> None:
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert make_tuple_set(subsets([1, 2, 3])) == make_tuple_set(expected)


def test_example_2() -> None:
    assert make_tuple_set(subsets([0])) == make_tuple_set([[], [0]])
