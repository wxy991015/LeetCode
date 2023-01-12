from typing import Optional

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# version 1 - Does not work properly
def flatten(head: 'Optional[Node]') -> 'Optional[Node]':
    p = Node(0)
    result = p
    current = head
    while current:
        if current.child == None:
            p.next = Node(current.val)
        else:
            temp = current
            while temp:
                p.next = flatten(temp)
                temp = temp.next
        p = p.next
        current = current.next
    return result.next

# version 2 - use stack
