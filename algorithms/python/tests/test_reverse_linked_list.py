from definitions.list_node import ListNode
from problems.reverse_linked_list import reverse_list


def test_example_1() -> None:
    assert reverse_list(ListNode.from_vals([1, 2])).to_vals() == [2, 1]  # type: ignore


def test_example_2() -> None:
    assert reverse_list(None) is None
