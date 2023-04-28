from typing import Dict


class LRUCache:
    def __init__(self, capacity: int):
        self.cache: Dict[int, int] = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            del self.cache[next(iter(self.cache))]
        self.cache[key] = value
