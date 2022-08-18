from problems.word_search import exist


def test_example_1() -> None:
    assert (
        exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
        is True
    )


def test_example_2() -> None:
    assert (
        exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
        is True
    )


def test_example_3() -> None:
    assert (
        exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
        is False
    )


def test_small() -> None:
    assert exist([["a", "a"]], "a") is True
