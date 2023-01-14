from typing import Optional

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert(head: 'Optional[Node]', insertVal: int) -> 'Node':
    if not head:
        head = Node(insertVal)
        return head
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