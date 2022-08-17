from itertools import chain

from problems.largest_rectangle_in_histogram import largest_rectangle_area


def test_example_1():
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10


def test_example_2():
    assert largest_rectangle_area([2, 4]) == 4


def test_zero():
    assert largest_rectangle_area([0]) == 0


def test_one():
    assert largest_rectangle_area([1]) == 1


def test_two():
    assert largest_rectangle_area([2]) == 2


def test_many_ones():
    assert largest_rectangle_area([1] * 30_000) == 30_000


def test_two_one_two():
    assert largest_rectangle_area([2, 1, 2]) == 3


def test_large():
    heights = list(chain.from_iterable(10 * [i] for i in range(10_000)))
    assert largest_rectangle_area(heights) == 250_000_000


def test_four_two():
    assert largest_rectangle_area([4, 2]) == 4


def test_large_range():
    assert largest_rectangle_area(list(range(24_000))) == 144_000_000


def test_snake_eyes():
    assert largest_rectangle_area([1, 1]) == 2
