"""
Xiaoyang Wei's first Hard Level Issue of LeetCode
LeetCode Problem 25
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    return head