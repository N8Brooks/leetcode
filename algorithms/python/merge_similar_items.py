from typing import List


def merge_similar_items(
    items1: List[List[int]], items2: List[List[int]]
) -> List[List[int]]:
    items = dict(items1)  # type: ignore
    for key, val in items2:
        items[key] = items.get(key, 0) + val
    return sorted(map(list, items.items()))


def test_example_1():
    assert merge_similar_items([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]) == [
        [1, 6],
        [3, 9],
        [4, 5],
    ]


def test_example_2():
    assert merge_similar_items([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]]) == [
        [1, 4],
        [2, 4],
        [3, 4],
    ]


def test_example_3():
    assert merge_similar_items([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]]) == [
        [1, 7],
        [2, 4],
        [7, 1],
    ]
