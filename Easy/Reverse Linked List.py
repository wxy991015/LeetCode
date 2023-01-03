from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    p = ListNode()
    reversed_result = p
    p.next = ListNode(val=head.val)
    head = head.next
    while head:
        node = ListNode(head.val)
        node.next = p.next
        p.next = node
        head = head.next
    reversed_result = reversed_result.next
    return reversed_result