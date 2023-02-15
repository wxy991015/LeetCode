"""
Xiaoyang Wei's first Hard Level Issue of LeetCode
LeetCode Problem 25
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - brute force
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    i = 0
    while i + k <= len(nodes):
        nodes[i:i+k] = nodes[i:i+k][::-1]
        i += k
    p = ListNode()
    res = p
    for i in nodes:
        p.next = ListNode(i)
        p = p.next
    return res.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 3
res = reverseKGroup(head, k)
while res:
    print(res.val)
    res = res.next