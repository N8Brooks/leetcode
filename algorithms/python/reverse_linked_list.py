from typing import Optional

from .definitions.list_node import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    previous_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node


def test_example_1() -> None:
    assert reverse_list(ListNode.from_vals([1, 2])).to_vals() == [2, 1]  # type: ignore


def test_example_2() -> None:
    assert reverse_list(None) is None
