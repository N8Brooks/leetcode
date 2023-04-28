from collections import Counter
from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)
    counts = Counter(tasks)
    max_freq = max(counts.values())
    count = sum(freq == max_freq for freq in counts.values())
    return max(len(tasks), (max_freq - 1) * (n + 1) + count)
