from typing import List


def num_islands(grid: List[List[str]]) -> int:
    def find(i):
        return i if parent.get(i, i) == i else find(parent[i])

    rows = len(grid)
    cols = len(grid[0])
    parent = {}
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "0":
                continue
            loc = parent[i * cols + j] = find(i * cols + j)
            if i + 1 < rows and grid[i + 1][j] == "1":
                parent[find((i + 1) * cols + j)] = loc
            if j + 1 < cols and grid[i][j + 1] == "1":
                parent[find(i * cols + j + 1)] = loc
    return len(frozenset(map(find, parent)))


def test_example_1() -> None:
    assert (
        num_islands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )


def test_example_2() -> None:
    assert (
        num_islands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )


def test_one() -> None:
    assert num_islands([["1"]]) == 1
