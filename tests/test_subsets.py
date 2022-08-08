import pytest
from problems.subsets import solution


def make_tuple_set(subsets):
    return set(tuple(subset) for subset in subsets)


def test_example_1():
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert make_tuple_set(solution([1, 2, 3])) == make_tuple_set(expected)


def test_example_2():
    assert make_tuple_set(solution([0])) == make_tuple_set([[], [0]])
