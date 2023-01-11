import math
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    k_parts_result = [None] * k
    current_index = 0
    nodes = 0
    p = head
    while p:
        nodes += 1
        p = p.next
    num_components = nodes // k
    components_remain = nodes % k
    current = head
    while current:
        temp = ListNode()
        p = temp
        count = 0
        while count < num_components and current:
            temp.next = ListNode(current.val)
            count += 1
            current = current.next
            temp = temp.next
        if components_remain != 0:
            temp.next = ListNode(current.val)
            temp = temp.next
            components_remain -= 1
        p = p.next
        k_parts_result[current_index] = p
        current_index += 1
    return k_parts_result