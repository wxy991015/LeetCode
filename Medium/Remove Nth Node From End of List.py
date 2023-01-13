from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def listSize(head: Optional[ListNode]):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
    size = listSize(head)
    if size == 1:
        return None
    if size == n:
        return head.next
    pos = size - n
    count = 1
    current = head
    while count != pos:
        count += 1
        current = current.next
    current.next = current.next.next
    return head