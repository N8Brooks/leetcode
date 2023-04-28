from problems.insert_interval import insert


def test_example_1() -> None:
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]


def test_example_2() -> None:
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]


def test_empty() -> None:
    assert insert([], [5, 7]) == [[5, 7]]


def test_prepend() -> None:
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]


def test_append() -> None:
    assert insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]


def test_replace_last() -> None:
    assert insert([[0, 5], [9, 12]], [7, 16]) == [[0, 5], [7, 16]]


def test_replace_first() -> None:
    assert insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]


def test_replace_only() -> None:
    assert insert([[1, 5]], [2, 7]) == [[1, 7]]
