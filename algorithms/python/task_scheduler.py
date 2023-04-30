from collections import Counter
from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)
    counts = Counter(tasks)
    max_freq = max(counts.values())
    count = sum(freq == max_freq for freq in counts.values())
    return max(len(tasks), (max_freq - 1) * (n + 1) + count)


def test_example_1() -> None:
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8


def test_example_2() -> None:
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6


def test_example_3() -> None:
    assert (
        least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
        == 16
    )
