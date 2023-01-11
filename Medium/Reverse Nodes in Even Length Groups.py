from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseEvenLengthGroups(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        result = reverse(head.next)
        head.next.next = head
        head.next = None
        return result
    current = head
    temp_result = ListNode()
    result = temp_result
    group_length = 1
    while current:
        current_length = 0
        p = ListNode()
        temp = p
        while current_length != group_length and current:
            p.next = ListNode(current.val)
            p = p.next
            current = current.next
            current_length += 1
        temp = temp.next
        if current_length % 2 == 0:
            temp = reverse(temp)
        while temp:
            temp_result.next = ListNode(temp.val)
            temp_result = temp_result.next
            temp = temp.next
        group_length += 1
    return result.next