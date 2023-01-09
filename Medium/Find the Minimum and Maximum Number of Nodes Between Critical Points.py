from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodesBetweenCriticalPoints(head: Optional[ListNode]) -> list[int]:
    result = [-1, -1]
    return result