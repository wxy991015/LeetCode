from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    current = head
    after = current.next
    while current.next and after.next:
        temp = current.val
        current.val = after.val
        after.val = temp
        current = current.next.next
        after = current.next
    if current and after:
        temp = current.val
        current.val = after.val
        after.val = temp
    return head