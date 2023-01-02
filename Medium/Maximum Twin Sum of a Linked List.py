from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head: Optional[ListNode]) -> int:
    maximum_twin_sum = 0
    nodes = []
    temp = head
    # get all values from linked list head
    while temp:
        nodes.append(temp.val)
        temp = temp.next
    i, j = 0, len(nodes) - 1
    while i < j:
        twin_sum = nodes[i] + nodes[j]
        maximum_twin_sum = max(maximum_twin_sum, twin_sum)
        i += 1
        j -= 1
    return maximum_twin_sum

