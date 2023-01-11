from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    before = ListNode()
    after = ListNode()
    p = before
    q = after
    while head:
        if head.val < x:
            p.next = ListNode(head.val)
            p = p.next
        else:
            q.next = ListNode(head.val)
            q = q.next
        head = head.next
    after = after.next
    p.next = after
    before = before.next
    return before