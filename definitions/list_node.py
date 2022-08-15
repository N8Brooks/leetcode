from __future__ import annotations

from typing import List, Optional


class ListNode:
    """Definition for singly-linked list"""

    # pylint: disable=redefined-builtin
    def __init__(self, x: int = 0, next: Optional[ListNode] = None):
        self.val = x
        self.next = next

    @staticmethod
    def from_vals(vals: List[int], pos: Optional[int] = None) -> ListNode:
        """Creates a linked list from `vals` in order"""
        head = node = ListNode(None)
        for val in vals:
            node.next = node = ListNode(val)
        if pos is not None:
            nth = head
            for _ in range(pos):
                nth = nth.next
            node.next = nth
        return head.next

    def to_vals(self) -> List[int]:
        """Converts a singly-linked list to a python `list`"""
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result
