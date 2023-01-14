from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    p = result
    digit_sum = 0
    while l1 and l2:
        temp_sum = l1.val + l2.val
        
        if temp_sum < 10:
            digit_sum += temp_sum
        else:
            
            
        l1 = l1.next
        l2 = l2.next