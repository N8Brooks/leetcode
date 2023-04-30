import heapq
from operator import attrgetter
from typing import List, Optional

from .definitions.list_node import ListNode


def iter_list(node):
    while node:
        yield node
        node = node.next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    root = a = ListNode()
    for b in heapq.merge(*map(iter_list, lists), key=attrgetter("val")):
        a.next = a = b
    return root.next


def test_example_1() -> None:
    lists = [
        ListNode.from_vals([1, 4, 5]),
        ListNode.from_vals([1, 3, 4]),
        ListNode.from_vals([2, 6]),
    ]
    actual = merge_k_lists(lists).to_vals()  # type: ignore
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert actual == expected
