import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def iter_list(node):
    while node:
        yield node
        node = node.next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    root = a = ListNode()
    for b in heapq.merge(*map(iter_list, lists), key=lambda x: x.val):
        a.next = a = b
    return root.next
