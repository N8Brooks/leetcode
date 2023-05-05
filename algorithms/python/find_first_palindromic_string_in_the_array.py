from typing import List


def first_palindrome(words: List[str]) -> str:
    return next((word for word in words if word == word[::-1]), "")


def test_example_1():
    assert first_palindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada"


def test_example_2():
    assert first_palindrome(["notapalindrome", "racecar"]) == "racecar"


def test_example_3():
    assert first_palindrome(["def", "ghi"]) == ""
