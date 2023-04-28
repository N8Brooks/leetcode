from definitions.list_node import ListNode
from problems.merge_k_sorted_lists import merge_k_lists


def test_example_1() -> None:
    lists = [
        ListNode.from_vals([1, 4, 5]),
        ListNode.from_vals([1, 3, 4]),
        ListNode.from_vals([2, 6]),
    ]
    actual = merge_k_lists(lists).to_vals()  # type: ignore
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert actual == expected
