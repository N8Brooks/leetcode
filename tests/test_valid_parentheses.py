import pytest
from problems.valid_parentheses import solution


def test_example_1():
    assert solution("()") == True


def test_example_2():
    assert solution("()[]{}") == True


def test_example_3():
    assert solution("(]") == False
