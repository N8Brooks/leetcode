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
