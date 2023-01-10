from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def numComponents(head: Optional[ListNode], nums: list[int]) -> int:
    connected_components = 0
    
    return connected_components