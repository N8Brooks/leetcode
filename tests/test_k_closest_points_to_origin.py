import pytest
from problems.k_closest_points_to_origin import k_closest


def test_example_1():
    assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]


def test_example_2():
    assert k_closest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
