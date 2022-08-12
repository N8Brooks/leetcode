from problems.lru_cache import LRUCache


def assert_input_correct(instructions, values):
    cache: LRUCache
    for instruction, value in zip(instructions, values):
        if instruction == "LRUCache":
            cache = LRUCache(value[0])
        elif instruction == "get":
            assert cache.get(value[0]) == value[1]
        elif instruction == "put":
            cache.put(value[0], value[1])
        else:
            raise Exception(f"{instruction} is not a valid instruction")


def test_example_1():
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


def test_get_put_get():
    assert_input_correct(
        ["LRUCache", "put", "put", "get", "put", "get", "get"],
        [[2], [2, 1], [1, 1], [2, 1], [4, 1], [1, -1], [2, 1]],
    )


def test_put_put_get():
    assert_input_correct(
        ["LRUCache", "put", "put", "get", "put", "put", "get"],
        [[2], [2, 1], [2, 2], [2, 2], [1, 1], [4, 1], [2, -1]],
    )


def test_put_put_get_get():
    assert_input_correct(
        ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
        [[2], [2, -1], [2, 6], [1, -1], [1, 5], [1, 2], [1, 2], [2, 6]],
    )


def test_put_get_get():
    assert_input_correct(
        ["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
        [[2], [2, -1], [2, 6], [1, -1], [1, 5], [1, 2], [1, 2], [2, 6]],
    )


def test_put_put_put_get():
    assert_input_correct(
        ["LRUCache", "put", "put", "put", "put", "get", "get"],
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1, -1], [2, 3]],
    )
