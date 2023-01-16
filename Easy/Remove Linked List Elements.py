from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - create a head
def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head == None:
        return head
    p = ListNode(-1, head)
    result = p
    while p.next:
        if p.next.val == val:
            p.next = p.next.next
        else:
            p = p.next
    return result.next

# version 2 - remove head if equal to val
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head == None:
        return head
    while head and head.val == val:
        head = head.next
    current = head
    while current:
        if current.next and current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return head