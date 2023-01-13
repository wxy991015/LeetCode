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
def flatten1(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head: return head
    dummy = Node(0)
    cur, stack = dummy, [head]
    while stack:
        tmp = stack.pop()
        if tmp.next: stack.append(tmp.next)
        if tmp.child: stack.append(tmp.child)
        cur.next = tmp
        tmp.prev = cur
        tmp.child = None
        cur = tmp
    dummy.next.prev = None
    return dummy.next

"""
head ==>
1 --> 2 --> 3 --> 4 --> 5 --> 6
            7 --> 8 --> 9 --> 10
                  11 --> 12

stack = [head]
tmp = head
stack = []
stack = [2 --> ]
current = 0 --> head
tmp.child = None
current = tmp
"""