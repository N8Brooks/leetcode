import pytest
from problems.merge_k_sorted_lists import ListNode, merge_k_lists


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def from_list(vals):
    head = node = ListNode()
    for val in vals:
        node.next = node = ListNode(val)
    return head.next


def test_example_1():
    lists = [
        from_list([1, 4, 5]),
        from_list([1, 3, 4]),
        from_list([2, 6]),
    ]
    assert to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
