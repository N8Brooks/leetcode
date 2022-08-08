from typing import Optional

from definitions.list_node import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    a = head
    b = head and head.next
    while b and b.next and a != b:
        a = a.next
        b = b.next.next
    return b and a == b
