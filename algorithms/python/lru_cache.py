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


def assert_input_correct(instructions, values):
    cache: LRUCache
    for instruction, value in zip(instructions, values):
        match instruction:
            case "LRUCache":
                cache = LRUCache(value[0])
            case "get":
                assert cache.get(value[0]) == value[1]
            case "put":
                cache.put(value[0], value[1])
            case _:
                raise ValueError(f"{instruction} is not a valid instruction")


def test_example_1() -> None:
    assert_input_correct(
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [
            [2, 2],
            [1, 1],
            [2, 2],
            [1, 1],
            [3, 3],
            [2, -1],
            [4, 4],
            [1, -1],
            [3, 3],
            [4, 4],
        ],
    )


def test_get_put_get() -> None:
    assert_input_correct(
        ["LRUCache", "put", "put", "get", "put", "get", "get"],
        [[2], [2, 1], [1, 1], [2, 1], [4, 1], [1, -1], [2, 1]],
    )


def test_put_put_get() -> None:
    assert_input_correct(
        ["LRUCache", "put", "put", "get", "put", "put", "get"],
        [[2], [2, 1], [2, 2], [2, 2], [1, 1], [4, 1], [2, -1]],
    )


def test_put_put_get_get() -> None:
    assert_input_correct(
        ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
        [[2], [2, -1], [2, 6], [1, -1], [1, 5], [1, 2], [1, 2], [2, 6]],
    )


def test_put_get_get() -> None:
    assert_input_correct(
        ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
        [[2], [2, -1], [2, 6], [1, -1], [1, 5], [1, 2], [1, 2], [2, 6]],
    )


def test_put_put_put_get() -> None:
    assert_input_correct(
        ["LRUCache", "put", "put", "put", "put", "get", "get"],
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1, -1], [2, 3]],
    )
