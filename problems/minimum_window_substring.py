from collections import Counter
from typing import Generator


def iter_windows(s: str, t: str) -> Generator[slice, None, None]:
    i = 0
    counts = Counter(t)
    total = len(t)
    for j, char in enumerate(s):
        if char in counts:
            total -= counts[char] > 0
            counts[char] -= 1
        while total == 0:
            char = s[i]
            if char in counts:
                yield slice(i, j + 1)
                counts[char] += 1
                total += counts[char] > 0
            i += 1


def len_window(window: slice) -> int:
    return window.stop - window.start


def min_window(s: str, t: str) -> str:
    return s[min(iter_windows(s, t), key=len_window, default=slice(0, 0))]
