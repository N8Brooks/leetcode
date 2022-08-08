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
    return ["".join(chars) for chars in product(*map(DIGITS.get, digits)) if chars]
