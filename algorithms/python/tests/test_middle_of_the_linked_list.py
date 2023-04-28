from definitions.list_node import ListNode
from problems.middle_of_the_linked_list import middle_node

# mypy: ignore-errors


def test_example_1() -> None:
    assert middle_node(ListNode.from_vals([1, 2, 3, 4, 5])).to_vals() == [3, 4, 5]


def test_example_2() -> None:
    assert middle_node(ListNode.from_vals([1, 2, 3, 4, 5, 6])).to_vals() == [4, 5, 6]
