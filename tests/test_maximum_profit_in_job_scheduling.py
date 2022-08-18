from problems.maximum_profit_in_job_scheduling import job_scheduling


def test_example_1() -> None:
    assert job_scheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120


def test_example_2() -> None:
    assert (
        job_scheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]) == 150
    )


def test_example_3() -> None:
    assert job_scheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6
