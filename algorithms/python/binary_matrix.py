from typing import List

# fmt: off

def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    flooded = {(x, y) for y, row in enumerate(mat) for x, bit in enumerate(row) if not bit}
    result: List[List[int]] = [[None] * len(mat[0]) for _ in mat] # type: ignore
    distance = 0
    while flooded:
        for x, y in flooded:
            result[y][x] = distance
        flooded = {
            (x, y)
            for x, y in flooded
            for x, y in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
            if 0 <= x < len(mat[0]) and 0 <= y < len(mat) and result[y][x] is None
        }
        distance += 1
    return result


def test_example_1() -> None:
    actual = update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert actual == expected


def test_example_2() -> None:
    actual = update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert actual == expected


def test_small() -> None:
    actual = update_matrix([[0], [1]])
    expected = [[0], [1]]
    assert actual == expected
