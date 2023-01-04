from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    value = []
    while head:
        value.append(head.val)
        head = head.next
    value.sort()
    sorted_linked_list = ListNode()
    result = sorted_linked_list
    for i in value:
        sorted_linked_list.next = ListNode(i)
        sorted_linked_list = sorted_linked_list.next
    return result.next