import bisect
from typing import List


def job_scheduling(
    start_times: List[int], end_times: List[int], profit_amounts: List[int]
) -> int:
    jobs = sorted(zip(start_times, end_times, profit_amounts), key=lambda job: job[1])
    previous_profit = 0
    times = [0]
    profits = [previous_profit]
    for start, end, profit in jobs:
        i = bisect.bisect(times, start)
        current_profit = profits[i - 1] + profit
        if current_profit > previous_profit:
            previous_profit = current_profit
            times.append(end)
            profits.append(previous_profit)
    return previous_profit


def test_example_1() -> None:
    assert job_scheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120


def test_example_2() -> None:
    assert (
        job_scheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]) == 150
    )


def test_example_3() -> None:
    assert job_scheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6
