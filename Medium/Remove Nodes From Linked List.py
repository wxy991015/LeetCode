from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - Does not work properly
def removeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    p = ListNode(0, head)
    current = p.next
    while current:
        temp = current
        while temp:
            if temp.val > current.val:
                p.next = current.next
                break
            temp = temp.next
        current = current.next
    return head

# version 2 - Work but time exceed the time
# creating new nodes might take longer time
def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    p = ListNode()
    result = p
    current, after = head, head.next
    while head.next:
        temp = current
        flag = True
        while after:
            if after.val > temp.val:
                flag = False
                break
            after = after.next
        if flag:
            p.next = ListNode(current.val)
            p = p.next
        current = current.next
        after = current.next
        head = head.next
    p.next = ListNode(head.val)
    return result.next

# version 3
# Try to delete nodes inside original list instead of creating new list
