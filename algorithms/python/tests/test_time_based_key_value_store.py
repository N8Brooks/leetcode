from problems.time_based_key_value_store import TimeMap


def assert_input_correct(instructions, values):
    time_map: TimeMap
    for instruction, value in zip(instructions, values):
        match instruction:
            case "TimeMap":
                time_map = TimeMap()
            case "set":
                time_map.set(*value)
            case "get":
                assert time_map.get(value[0], value[1]) == value[2]
            case _:
                raise ValueError(f"{instruction} is not a valid instruction")


def test_example_1() -> None:
    assert_input_correct(
        ["TimeMap", "set", "get", "get", "set", "get", "get"],
        [
            [],
            ["foo", "bar", 1],
            ["foo", 1, "bar"],
            ["foo", 3, "bar"],
            ["foo", "bar2", 4],
            ["foo", 4, "bar2"],
            ["foo", 5, "bar2"],
        ],
    )


def test_numbers() -> None:
    assert_input_correct(
        ["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
        [
            [],
            ["love", "high", 10],
            ["love", "low", 20],
            ["love", 5, ""],
            ["love", 10, "high"],
            ["love", 15, "high"],
            ["love", 20, "low"],
            ["love", 25, "low"],
        ],
    )


# pylint: disable=line-too-long
def test_zs() -> None:
    assert_input_correct(
        ["TimeMap", "set", "get", "get", "set", "get", "get"],
        [
            [],
            [
                "foo",
                "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
                1,
            ],
            [
                "foo",
                1,
                "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
            ],
            [
                "foo",
                3,
                "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
            ],
            ["foo", "bar2", 4],
            ["foo", 4, "bar2"],
            ["foo", 5, "bar2"],
        ],
    )
