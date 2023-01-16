from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    nodes = dict()
    p = head
    current = head
    result = ListNode()
    prev = result
    while p:
        nodes[p.val] = nodes.get(p.val, 0) + 1
        p = p.next
    aux = {k for k, v in nodes.items() if v > 1}
    while current:
        while current and current.val in aux:
            current = current.next
        prev.next = current
        if current:
            prev = current
            current = current.next
    return result.next