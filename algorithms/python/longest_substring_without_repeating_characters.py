def length_of_longest_substring(s: str) -> int:
    i = length = 0
    for j, char in enumerate(s):
        i = max(i, s.rfind(char, i, j) + 1)
        length = max(length, j - i + 1)
    return length


def test_example_1() -> None:
    assert length_of_longest_substring("abcabcbb") == 3


def test_example_2() -> None:
    assert length_of_longest_substring("bbbbb") == 1


def test_example_3() -> None:
    assert length_of_longest_substring("pwwkew") == 3
