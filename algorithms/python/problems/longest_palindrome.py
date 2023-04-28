from collections import Counter


def longest_palindrome(s: str) -> int:
    longest = 0
    for count in Counter(s).values():
        is_odd = count & 1
        longest += count - is_odd
        longest |= is_odd
    return longest
