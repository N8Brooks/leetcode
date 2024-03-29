from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        group = "".join(sorted(word))
        groups[group].append(word)
    return list(groups.values())


def test_example_1():
    actual = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    actual = sorted(sorted(group) for group in actual)
    expected = sorted(sorted(group) for group in expected)
    assert actual == expected


def test_example_2():
    assert group_anagrams([""]) == [[""]]


def test_example_3():
    assert group_anagrams(["a"]) == [["a"]]
