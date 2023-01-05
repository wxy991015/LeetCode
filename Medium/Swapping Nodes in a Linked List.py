from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    size = 0
    p, end, swap_result = head, head, head
    while head:
        size += 1
        head = head.next
    beginning_k, end_k = k, size - k
    i = 1
    head = p
    while 
    return swap_result
