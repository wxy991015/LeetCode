from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    p = ListNode()
    p.next = head
    current = p
    while current:
        temp = current
        while temp:
            if temp.val > current.val:
                p.next = current.next
                break
        current = current.next
    return head