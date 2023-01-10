from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    # do not forget to check whether head is empty
    if head == None:
        return head
    list_nodes = []
    while head:
        list_nodes.append(head.val)
        head = head.next
    list_nodes = sorted(list_nodes)
    p = ListNode()
    result = p
    for i in range(len(list_nodes)):
        p.next = ListNode(list_nodes[i])
        p = p.next
    return result.next

# version 2
def sortList1(head: Optional[ListNode]) -> Optional[ListNode]:
    # do not forget to check whether head is empty
    if head == None:
        return head
    list_nodes = []
    while head:
        list_nodes.append(head.val)
        head = head.next
    list_nodes = sorted(list_nodes)
    p = ListNode()
    result = p
    for i in range(len(list_nodes)):
        p.next = ListNode(list_nodes[i])
        p = p.next
    return result.next