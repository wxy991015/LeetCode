from typing import Optional

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert(head: 'Optional[Node]', insertVal: int) -> 'Node':
    if not head:
        node = Node(insertVal)
        head = node
        node.next = head
        return head
    """
    if not head.next:
        head.next = Node(insertVal)
        return head
    prev = head
    after = head.next
    while prev:
        if prev.val <= insertVal and after.val >= insertVal:
            prev.next = Node(insertVal)
            prev.next.next = after
            break
        prev = prev.next
        after = after.next
    return head
    """
    original_head = head
    while head:
        if head.next.val > head.val:
            if insertVal >= head.val and insertVal <= head.next.val:
                break
        elif head.next.val < head.val:
            if insertVal >= head.val or insertVal <= head.next.val:
                break
        elif head.next == original_head:
            break
        head = head.next
    head.next = Node(insertVal, head.next)
    return head