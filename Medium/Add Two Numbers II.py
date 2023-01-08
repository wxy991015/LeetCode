from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def listToNum(l: Optional[ListNode]):
        num = 0
        while l:
            num += num * 10 + l.val
            l = l.next
        return num
    total_sum = listToNum(l1) + listToNum(l2)
    digits = [int(d) for d in str(total_sum)]
    p = ListNode()
    result = p
    for i in digits:
        p.next = ListNode(i)
        p = p.next
    return result.next

# version 2