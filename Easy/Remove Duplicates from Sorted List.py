from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    p = ListNode(0, head)
    while head.next:
        if p.val == p.next.val:
            head.next = head.next.next
        head = head.next
    return p.next