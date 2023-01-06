from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
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

# version 2 - Faster
def sortLinkedList1(head: Optional[ListNode]) -> Optional[ListNode]:
    p = head
    while p.next:
        if p.val > p.next.val:
            temp = p.next
            # cut current node from original linked list
            p.next = temp.next
            # insert current node to the head
            temp.next = head
            head = temp # why I need to add this line?
        else:
            p = p.next
    return head