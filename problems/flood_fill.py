from typing import List


# pylint: disable=invalid-name
def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start = image[sr][sc]
    if color == start:
        return image
    fill = {(sr, sc)}
    while fill:
        r, c = fill.pop()
        if 0 <= c < len(image[0]) and 0 <= r < len(image) and image[r][c] == start:
            image[r][c] = color
            fill.update(
                (
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                )
            )
    return image
