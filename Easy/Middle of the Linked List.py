from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    head_copy = head
    size, start = 0, 0
    while head:
        size += 1
        head = head.next
    middle = size // 2
    while start < middle:
        head_copy = head_copy.next
        start += 1
    return head_copy

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(f"Output: {middleNode(head)}")