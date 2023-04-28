from problems.permutations_in_string import check_inclusion


def test_example_1():
    assert check_inclusion("ab", "eidbaooo") is True


def test_example_2():
    assert check_inclusion("ab", "eidboaoo") is False


def test_example_short():
    assert check_inclusion("adc", "dcda") is True


def test_example_long():
    assert check_inclusion("dinitrophenylhydrazine", "acetylphenylhydrazine") is False
