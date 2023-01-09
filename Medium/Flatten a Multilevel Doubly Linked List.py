from typing import Optional

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: 'Optional[Node]') -> 'Optional[Node]':
    return head