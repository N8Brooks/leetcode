from problems.find_all_anagrams_in_a_string import find_anagrams


def test_example_1():
    assert find_anagrams("cbaebabacd", "abc")


def test_example_2():
    assert find_anagrams("abab", "ab")
