from problems.valid_anagram import is_anagram


def test_example_1():
    assert is_anagram("anagram", "nagaram") is True


def test_example_2():
    # Example 2
    assert is_anagram("rat", "car") is False
