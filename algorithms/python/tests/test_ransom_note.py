from problems.ransom_note import can_construct


def test_example_1() -> None:
    assert can_construct("a", "b") is False


def test_example_2() -> None:
    assert can_construct("aa", "ab") is False


def test_example_3() -> None:
    assert can_construct("aa", "aab") is True
