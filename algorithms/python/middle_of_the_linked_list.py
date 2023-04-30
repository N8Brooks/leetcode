from typing import Optional

from .definitions.list_node import ListNode


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    a = b = head
    while b and b.next:
        a = a.next  # type: ignore
        b = b.next.next
    return a


# mypy: ignore-errors


def test_example_1() -> None:
    assert middle_node(ListNode.from_vals([1, 2, 3, 4, 5])).to_vals() == [3, 4, 5]


def test_example_2() -> None:
    assert middle_node(ListNode.from_vals([1, 2, 3, 4, 5, 6])).to_vals() == [4, 5, 6]
