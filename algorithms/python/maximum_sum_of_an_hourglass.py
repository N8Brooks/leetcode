from typing import List


def max_sum(grid: List[List[int]]) -> int:
    return max(
        sum(grid[i - 2][j - 2 : j + 1])
        + grid[i - 1][j - 1]
        + sum(grid[i][j - 2 : j + 1])
        for i in range(2, len(grid))
        for j in range(2, len(grid[0]))
    )


def test_example_1():
    assert max_sum([[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]) == 30


def test_example_2():
    assert max_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 35


def test_rectangle():
    assert (
        max_sum(
            [
                [520626, 685427, 788912, 800638, 717251, 683428],
                [23602, 608915, 697585, 957500, 154778, 209236],
                [287585, 588801, 818234, 73530, 939116, 252369],
            ]
        )
        == 5095181
    )
