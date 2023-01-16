from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    current = head
    while current:
        previous = result
        while previous.next and previous.next.val <= current.val:
            previous = previous.next
        after = current.next
        current.next = previous.next
        previous.next = current
        current = after
    return result.next