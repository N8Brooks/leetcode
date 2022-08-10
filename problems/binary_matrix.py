from typing import List


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    flooded = {
        (x, y) for y, row in enumerate(mat) for x, bit in enumerate(row) if not bit
    }
    res = [[None for _ in row] for row in mat]
    width = len(mat[0])
    height = len(mat)
    distance = 0
    while flooded:
        next_flooded = set()
        for x, y in flooded:
            res[y][x] = distance
            if x - 1 >= 0 and res[y][x - 1] is None:
                next_flooded.add((x - 1, y))
            if x + 1 < width and res[y][x + 1] is None:
                next_flooded.add((x + 1, y))
            if y - 1 >= 0 and res[y - 1][x] is None:
                next_flooded.add((x, y - 1))
            if y + 1 < height and res[y + 1][x] is None:
                next_flooded.add((x, y + 1))
        distance += 1
        flooded = next_flooded - flooded
    return res
