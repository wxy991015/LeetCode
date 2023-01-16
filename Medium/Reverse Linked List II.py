from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == right:
        return head
    result = ListNode(0)
    p = result
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    nodes[left-1:right] = nodes[left-1:right][::-1]
    for i in nodes:
        p.next = ListNode(i)
        p = p.next
    return result.next