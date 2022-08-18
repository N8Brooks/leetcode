from definitions.list_node import ListNode
from problems.merge_two_sorted_lists import merge_two_lists


def test_example_1() -> None:
    list1 = list2 = ListNode.from_vals([])
    actual = merge_two_lists(list1, list2)
    assert actual is None


def test_example_2() -> None:
    list1 = ListNode.from_vals([])
    list2 = ListNode.from_vals([0])
    assert merge_two_lists(list1, list2).to_vals() == [0]  # type: ignore
