from problems.longest_palindromic_substring import longest_palindrome


def test_example_1():
    assert longest_palindrome("babad") == "bab"


def test_example_2():
    assert longest_palindrome("cbbd") == "bb"


def test_a():
    assert longest_palindrome("a") == "a"


def test_last():
    assert longest_palindrome("abb") == "bb"


def test_empty():
    assert longest_palindrome("") == ""
