from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    sorted_list = head
    sorted_list.next = None
    unsorted_list = head.next
    current = head
    while unsorted_list:
        current_node = unsorted_list
        temp = unsorted_list.next
        current_node.next = None
        
    return head