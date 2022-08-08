import pytest
from problems.longest_substring_without_repeating_characters import solution


def test_example_1():
    assert solution("abcabcbb") == 3


def test_example_2():
    assert solution("bbbbb") == 1


def test_example_3():
    assert solution("pwwkew") == 3
