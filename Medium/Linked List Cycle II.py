from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    hashSet = set()
    while head:
        if head in hashSet:
            return head
        hashSet.add(head)
        head = head.next
    return None