from typing import List


def row_and_maximum_ones(mat: List[List[int]]) -> List[int]:
    return list(max(enumerate(map(sum, mat)), key=lambda item: item[1]))  # type: ignore


def test_example_1():
    assert row_and_maximum_ones([[0, 1], [1, 0]]) == [0, 1]


def test_example_2():
    assert row_and_maximum_ones([[0, 0, 0], [0, 1, 1]]) == [1, 2]


def test_example_3():
    assert row_and_maximum_ones([[0, 0], [1, 1], [0, 0]]) == [1, 2]
