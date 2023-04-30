from typing import List


def read_binary_watch(turned_on: int) -> List[str]:
    return [
        f"{h}:{m:02}"
        for h in range(12)
        for m in range(60)
        if h.bit_count() + m.bit_count() == turned_on
    ]


def test_example_1() -> None:
    assert read_binary_watch(1) == [
        "0:01",
        "0:02",
        "0:04",
        "0:08",
        "0:16",
        "0:32",
        "1:00",
        "2:00",
        "4:00",
        "8:00",
    ]


def test_example_2() -> None:
    assert read_binary_watch(9) == []


def test_example_3() -> None:
    assert read_binary_watch(0) == ["0:00"]
