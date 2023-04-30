from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1
    while numbers[i] + numbers[j] != target:
        if numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
    return [i + 1, j + 1]


def test_example_1():
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]


def test_example_2():
    assert two_sum([2, 3, 4], 6) == [1, 3]


def test_example_3():
    assert two_sum([-1, 0], -1) == [1, 2]
