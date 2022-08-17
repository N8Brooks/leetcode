from typing import List


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    flooded = {
        (x, y) for y, row in enumerate(mat) for x, bit in enumerate(row) if not bit
    }
    result = [[None] * len(mat[0]) for _ in mat]
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
