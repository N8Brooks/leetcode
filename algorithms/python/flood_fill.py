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
            fill.update(((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)))
    return image


def test_example_1() -> None:
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    expected = flood_fill(image, sr=1, sc=1, color=2)
    actual = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert actual == expected


def test_example_2() -> None:
    image = [[0, 0, 0], [0, 0, 0]]
    expected = flood_fill(image, sr=0, sc=0, color=0)
    actual = [[0, 0, 0], [0, 0, 0]]
    assert actual == expected
