from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    hashSet = set()
    while head:
        if head in hashSet:
            return True
        hashSet.add(head)
        head = head.next
    return False