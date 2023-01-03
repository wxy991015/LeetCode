from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode) -> int:
    decimal_value = 0
    while head:
        decimal_value = decimal_value * 2 + head.val
        head = head.next
    return decimal_value

head: List[ListNode] = [1,0,1]
print(f"Output: {getDecimalValue(head)}")