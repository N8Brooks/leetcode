from definitions.list_node import ListNode
from problems.linked_list_cycle import has_cycle


def test_example_1() -> None:
    head = ListNode.from_vals([3, 2, 0, -4], 1)
    assert has_cycle(head) is True


def test_example_2() -> None:
    head = ListNode.from_vals([3, 2, 0, -4], 1)
    assert has_cycle(head) is True


def test_example_3() -> None:
    head = ListNode.from_vals([3, 2, 0, -4], 1)
    assert has_cycle(head) is True
