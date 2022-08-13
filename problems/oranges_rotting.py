from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    length = len(grid)
    width = len(grid[0])
    rotten = frozenset(
        (x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == 2
    )
    minutes = int(not rotten)
    while rotten:
        neighbors = (
            cell
            for x, y in rotten
            for cell in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
        )
        rotten = frozenset(
            (x, y)
            for x, y in neighbors
            if 0 <= x < width and 0 <= y < length and grid[y][x] == 1
        )
        for x, y in rotten:
            grid[y][x] = 2
        minutes += 1
    return -1 if any(cell == 1 for row in grid for cell in row) else minutes - 1
