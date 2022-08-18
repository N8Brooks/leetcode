from problems.longest_substring_without_repeating_characters import (
    length_of_longest_substring,
)


def test_example_1() -> None:
    assert length_of_longest_substring("abcabcbb") == 3


def test_example_2() -> None:
    assert length_of_longest_substring("bbbbb") == 1


def test_example_3() -> None:
    assert length_of_longest_substring("pwwkew") == 3
