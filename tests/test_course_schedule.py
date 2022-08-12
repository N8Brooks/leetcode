from problems.course_schedule import can_finish


def test_example_1():
    assert can_finish(2, [[1, 0]]) is True


def test_example_2():
    assert can_finish(2, [[1, 0], [0, 1]]) is False


def test_three():
    assert can_finish(3, [[1, 0], [1, 2], [0, 1]]) is False


def test_backwards():
    assert can_finish(2, [[0, 1]]) is True
