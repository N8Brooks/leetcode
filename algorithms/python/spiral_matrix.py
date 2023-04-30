from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    k = l = 0

    result = []
    while k < m and l < n:
        result.extend(matrix[k][l:n])
        k += 1

        n -= 1
        result.extend(matrix[i][n] for i in range(k, m))

        if k < m:
            m -= 1
            result.extend(reversed(matrix[m][l:n]))

        if l < n:
            result.extend(matrix[i][l] for i in range(m - 1, k - 1, -1))
            l += 1

    return result


def test_example_1() -> None:
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


def test_example_2() -> None:
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


def test_long() -> None:
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


def test_small() -> None:
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]


def test_vertical() -> None:
    assert spiral_order([[7], [9], [6]]) == [7, 9, 6]
