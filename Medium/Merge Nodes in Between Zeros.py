from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - Faster
def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    modified_result = ListNode()
    p = modified_result
    merged_nodes_sum = 0
    head = head.next
    while head:
        if head.val != 0:
            merged_nodes_sum += head.val
        else:
            p.next = ListNode(head.val)
            p = p.next
            merged_nodes_sum = 0
        head = head.next
    modified_result = modified_result.next
    return modified_result

# version 2
def mergeNodes1(head: Optional[ListNode]) -> Optional[ListNode]:
    p, current = head, head
    merged_nodes_sum = 0
    # begin is guaranteed to be zero, so go to next
    p = p.next
    while p: 
        if p.val == 0:
            current = current.next
            current.val = merged_nodes_sum
            merged_nodes_sum = 0
        else: merged_nodes_sum += p.val
        p = p.next
    current.next = None
    return head.next