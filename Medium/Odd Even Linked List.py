from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return head
    p, end = head, head
    size = 1
    while end.next:
        size += 1
        end = end.next
    count = 1
    current = p
    while count <= size:
        if count % 2 == 0:
            temp = current
            end.next = ListNode(temp.val)
            end = end.next
            p.next = current.next
            p = p.next
        current = current.next
        count += 1
    return head