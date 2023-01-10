from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    p = head.next
    reorder = []
    while p:
        reorder.append(p.val)
        p = p.next
    temp = ListNode()
    reordered_result = temp
    i = 0
    j = len(reorder) - 1
    while i <= j:
        temp.next = ListNode(reorder[j])
        temp.next = ListNode(reorder[i])
        temp = temp.next
        i += 1
        j -= 1
    reordered_result = reordered_result.next
    head.next = reordered_result