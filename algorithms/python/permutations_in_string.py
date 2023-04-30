from collections import Counter


def check_inclusion(s_1: str, s_2: str) -> bool:
    counts = Counter(s_1)
    counts.subtract(s_2[: len(s_1)])
    if not any(counts.values()):
        return True
    for i, char in enumerate(s_2[len(s_1) :]):
        counts[char] -= 1
        counts[s_2[i]] += 1
        if not any(counts.values()):
            return True
    return False


def test_example_1():
    assert check_inclusion("ab", "eidbaooo") is True


def test_example_2():
    assert check_inclusion("ab", "eidboaoo") is False


def test_example_short():
    assert check_inclusion("adc", "dcda") is True


def test_example_long():
    assert check_inclusion("dinitrophenylhydrazine", "acetylphenylhydrazine") is False
