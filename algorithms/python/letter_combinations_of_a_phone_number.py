from itertools import product
from typing import List

DIGITS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations(digits: str) -> List[str]:
    return (
        ["".join(chars) for chars in product(*(DIGITS[digit] for digit in digits))]
        if digits
        else []
    )


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
