from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - use list append, extend, and sort
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    p = ListNode()
    result = p
    k_linked_lists = []
    for i in lists:
        current_list = []
        while i:
            current_list.append(i.val)
            i = i.next
        k_linked_lists.extend(current_list)
    k_linked_lists.sort()
    for i in k_linked_lists:
        p.next = ListNode(i)
        p = p.next
    return result.next

# version 2 - use insertion sort
