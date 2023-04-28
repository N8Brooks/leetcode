import heapq
from operator import attrgetter
from typing import List, Optional

from definitions.list_node import ListNode


def iter_list(node):
    while node:
        yield node
        node = node.next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    root = a = ListNode()
    for b in heapq.merge(*map(iter_list, lists), key=attrgetter("val")):
        a.next = a = b
    return root.next
