from collections import Counter


def character_replacement(s: str, k: int) -> int:
    i = max_count = 0
    counts: Counter[str] = Counter()
    for char in s:
        counts[char] += 1
        if counts[char] > max_count:
            max_count = counts[char]
        else:
            k -= 1
        if k < 0:
            counts[s[i]] -= 1
            i += 1
            k += 1
    return len(s) - i


def test_example_1():
    assert character_replacement("ABAB", 2) == 4


def test_example_2():
    assert character_replacement("AABABBA", 1) == 4
