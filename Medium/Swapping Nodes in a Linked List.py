from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    size = 0
    p, end, swap_result = head, head, head
    while head:
        size += 1
        head = head.next
    beginning_k, end_k = k, size - k
    i, j = 1, 0
    head = p
    while i != beginning_k:
        head = head.next
    while j != end_k:
        end = end.next
    temp = head.val
    head.val = end.val
    end.val = temp
    return swap_result

# version 2
def swapNodes1(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    size = 0
    p, end, swap_result = head, head, head
    while head:
        size += 1
        head = head.next
    beginning_k, end_k = k, size - k
    i, j = 1, 0
    head = p
    while i != beginning_k:
        head = head.next
    while j != end_k:
        end = end.next
    temp = head.val
    head.val = end.val
    end.val = temp
    return swap_result