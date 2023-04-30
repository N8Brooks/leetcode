from typing import Optional

from .definitions.list_node import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    a = head
    b = head and head.next
    while b and b.next and a != b:
        a = a.next  # type: ignore
        b = b.next.next
    return bool(b) and a == b


def test_example_1() -> None:
    head = ListNode.from_vals([3, 2, 0, -4], 1)
    assert has_cycle(head) is True


def test_example_2() -> None:
    head = ListNode.from_vals([3, 2, 0, -4], 1)
    assert has_cycle(head) is True


def test_example_3() -> None:
    head = ListNode.from_vals([3, 2, 0, -4], 1)
    assert has_cycle(head) is True
