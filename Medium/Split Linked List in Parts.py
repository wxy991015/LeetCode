from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    k_parts_result = []
    return k_parts_result