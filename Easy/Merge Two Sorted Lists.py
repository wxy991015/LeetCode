from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - original version of merge
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    p = ListNode()
    merged_result = p
    while list1 and list2:
        if list1.val <= list2.val:
            p.next = ListNode(list1.val)
            list1 = list1.next
        else:
            p.next = ListNode(list2.val)
            list2 = list2.next
        p = p.next
    if list1:
        while list1:
            p.next = ListNode(list1.val)
            list1 = list1.next
            p = p.next
    if list2:
        while list2:
            p.next = ListNode(list2.val)
            list2 = list2.next
            p = p.next
    merged_result = merged_result.next
    return merged_result

# version 2 - updated version of merge
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    p = ListNode()
    merged_result = p
    while list1 and list2:
        if list1.val <= list2.val:
            p.next = list1
            list1 = list1.next
        else:
            p.next = list2
            list2 = list2.next
        p = p.next
    if list1:
        p.next = list1
    if list2:
        p.next = list2
    merged_result = merged_result.next
    return merged_result