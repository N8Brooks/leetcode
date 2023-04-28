from problems.task_scheduler import least_interval


def test_example_1() -> None:
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8


def test_example_2() -> None:
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6


def test_example_3() -> None:
    assert (
        least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
        == 16
    )
