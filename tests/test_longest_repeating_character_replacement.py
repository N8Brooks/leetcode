from problems.longest_repeating_character_replacement import (
    character_replacement,
)


def test_example_1():
    assert character_replacement("ABAB", 2) == 4


def test_example_2():
    assert character_replacement("AABABBA", 1) == 4
