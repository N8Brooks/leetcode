from problems.valid_anagram import is_anagram


def test_example_1() -> None:
    assert is_anagram("anagram", "nagaram") is True


def test_example_2() -> None:
    # Example 2
    assert is_anagram("rat", "car") is False
