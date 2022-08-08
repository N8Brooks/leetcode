from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    head = node = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            node.next = node = list1
            list1 = list1.next
        else:
            node.next = node = list2
            list2 = list2.next
    node.next = list1 if list1 else list2
    return head.next
