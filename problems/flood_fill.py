from typing import List


# pylint: disable=invalid-name
def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start = image[sr][sc]
    if color == start:
        return image
    fill = {(sr, sc)}
    while fill:
        r, c = fill.pop()
        image[r][c] = color
        if r - 1 >= 0 and image[r - 1][c] == start:
            fill.add((r - 1, c))
        if r + 1 < len(image) and image[r + 1][c] == start:
            fill.add((r + 1, c))
        if c - 1 >= 0 and image[r][c - 1] == start:
            fill.add((r, c - 1))
        if c + 1 < len(image[0]) and image[r][c + 1] == start:
            fill.add((r, c + 1))
    return image
