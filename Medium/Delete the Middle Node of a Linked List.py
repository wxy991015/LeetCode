from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    current = p = head
    size = 0
    while current:
        size += 1
        current = current.next
    if size == 1:
        return None
    middle = size // 2
    i = 1
    while i != middle:
        p = p.next
        i += 1
    p.next = p.next.next
    return head
    