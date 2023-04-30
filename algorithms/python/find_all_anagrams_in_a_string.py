from itertools import islice
from typing import List


def find_anagrams(s: str, p: str) -> List[int]:
    p_hash = sum(map(hash, p))
    s_hash = sum(map(hash, islice(s, 0, len(p))))
    result = [0] if p_hash == s_hash else []
    for i, char in enumerate(islice(s, len(p), None)):
        s_hash += hash(char) - hash(s[i])
        if p_hash == s_hash:
            result.append(i + 1)
    return result


def test_example_1() -> None:
    assert find_anagrams("cbaebabacd", "abc")


def test_example_2() -> None:
    assert find_anagrams("abab", "ab")
