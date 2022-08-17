from problems.spiral_matrix import spiral_order


def test_example_1():
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]


def test_example_2():
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]


def test_long():
    assert spiral_order(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
    ) == [
        1,
        2,
        3,
        4,
        5,
        10,
        15,
        20,
        25,
        24,
        23,
        22,
        21,
        16,
        11,
        6,
        7,
        8,
        9,
        14,
        19,
        18,
        17,
        12,
        13,
    ]


def test_small():
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]


def test_vertical():
    assert spiral_order([[7], [9], [6]]) == [7, 9, 6]
