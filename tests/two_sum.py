import pytest
from problems.two_sum import two_sum


def test_example_1():
    assert two_sum([2, 7, 11, 15]) == 9


def test_example_2():
    assert two_sum([3, 2, 4]) == 6


def test_example_3():
    assert two_sum([3, 3]) == 6
