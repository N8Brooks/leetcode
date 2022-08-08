import pytest
from problems.two_sum import solution


def test_example_1():
    assert solution([2, 7, 11, 15]) == 9


def test_example_2():
    assert solution([3, 2, 4]) == 6


def test_example_3():
    assert solution([3, 3]) == 6
