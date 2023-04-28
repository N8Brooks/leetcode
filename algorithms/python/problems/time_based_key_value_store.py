import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.cache:
            i = bisect.bisect(self.cache[key], (timestamp + 1,))
            value = self.cache[key][i - 1] if i > 0 else (None, "")
            return value[1]
        return ""
