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

# version 2 - Work but time limit exceeded
# creating new nodes might take longer time
def removeNodes1(head: Optional[ListNode]) -> Optional[ListNode]:
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
def removeNodes2(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(node, prev=None):
        if not node:
            return prev
        tmp = node.next
        node.next = prev
        return reverse(tmp, node)
    node = reverse(head)
    max_so_far = head.val
    dummy = ListNode(0)
    result = dummy
    while node:
        if max_so_far <= node.val:
            max_so_far = node.val
            result.next = ListNode(node.val)
            result = result.next
        node = node.next
    return reverse(dummy.next)