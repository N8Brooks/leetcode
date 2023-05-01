from collections import Counter
from itertools import chain, combinations
from typing import List


def powerset(iterable):
    "defined in itertools recipes"
    return chain.from_iterable(
        combinations(iterable, r) for r in range(len(iterable) + 1)
    )


def find_num_of_valid_words(words: List[str], puzzles: List[str]) -> List[int]:
    words = Counter(frozenset(word) for word in words)  # type: ignore
    return [
        sum(
            words[frozenset((puzzle[0],) + rest)]  # type: ignore
            for rest in powerset(puzzle[1:])
        )
        for puzzle in puzzles
    ]


def test_example_1():
    assert find_num_of_valid_words(
        ["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
        ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"],
    ) == [1, 1, 3, 2, 4, 0]


def test_example_2():
    assert find_num_of_valid_words(
        ["apple", "pleas", "please"],
        ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"],
    ) == [0, 1, 3, 2, 0]
