import pytest
from problems.subsets import subsets


def make_tuple_set(list_of_subsets):
    return set(tuple(subset) for subset in list_of_subsets)


def test_example_1():
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert make_tuple_set(subsets([1, 2, 3])) == make_tuple_set(expected)


def test_example_2():
    assert make_tuple_set(subsets([0])) == make_tuple_set([[], [0]])
