from collections import Counter


def longest_palindrome(s: str) -> int:
    longest = 0
    for count in Counter(s).values():
        is_odd = count & 1
        longest += count - is_odd
        longest |= is_odd
    return longest


def test_example_1() -> None:
    assert longest_palindrome("abccccdd") == 7


def test_example_2() -> None:
    assert longest_palindrome("a") == 1
