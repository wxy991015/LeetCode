from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# version 1 - hashset
def hasCycle(head: Optional[ListNode]) -> bool:
    hashSet = set()
    while head:
        if head in hashSet:
            return True
        hashSet.add(head)
        head = head.next
    return False

# version 2 - speed pointer
def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False
    s, t = head, head
    while s and t and t.next:
        if t.next == s:
            return True
        t = t.next.next
        s = s.next
    return False