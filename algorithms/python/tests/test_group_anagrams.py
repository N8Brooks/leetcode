from problems.group_anagrams import group_anagrams


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
