from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def rotate(head: Optional[ListNode]):
        current = head
        while current.next.next:
            current = current.next
        last_node = current.next
        current.next = None
        last_node.next = head
        return last_node
    if not head or not head.next:
        return head
    i = 0
    size = 0
    current = head
    while current:
        size += 1
        current = current.next
    rotation = k % size
    while i < rotation:
        head = rotate(head)
        i += 1
    return head