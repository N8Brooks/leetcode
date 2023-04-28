from typing import Optional

from definitions.list_node import ListNode


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    a = b = head
    while b and b.next:
        a = a.next  # type: ignore
        b = b.next.next
    return a
