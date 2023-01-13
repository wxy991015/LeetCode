from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    def reverse(head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        result = reverse(head.next)
        head.next.next = head
        head.next = None
        return result
    if left == right:
        return head
    count = 1
    start = head
    while count != left:
        start = start.next
        count += 1
    p = start
    while count != right:
        start = start.next
        count += 1
    start = reverse(p)
    return head