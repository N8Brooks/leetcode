from problems.letter_combinations_of_a_phone_number import letter_combinations


def test_example_1() -> None:
    assert letter_combinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]


def test_example_2() -> None:
    assert not letter_combinations("")


def test_example_3() -> None:
    assert letter_combinations("2") == ["a", "b", "c"]
