from definitions.list_node import ListNode
from problems.reverse_linked_list import reverse_list


def test_example_1():
    assert reverse_list(ListNode.from_vals([1, 2])).to_vals() == [2, 1]


def test_example_2():
    assert reverse_list(None) is None
