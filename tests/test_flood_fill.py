from problems.flood_fill import flood_fill


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
