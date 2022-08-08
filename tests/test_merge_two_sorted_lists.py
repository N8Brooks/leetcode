import pytest
from problems.merge_two_sorted_lists import ListNode, solution


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
    list1 = from_list([])
    list2 = from_list([])
    assert to_list(solution(list1, list2)) == []


def test_example_2():
    list1 = from_list([])
    list2 = from_list([0])
    assert to_list(solution(list1, list2)) == [0]
