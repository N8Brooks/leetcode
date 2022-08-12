from problems.first_bad_version import first_bad_version, set_bad_version


def test_example_1():
    set_bad_version(4)
    assert first_bad_version(5) == 4
