from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - time limit exceeded
def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    while True:
        consecutive_sequences = []
        start, end = 0, 0
        flag = False
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)+1):
                temp_sequence = nodes[i:j]
                if sum(temp_sequence) == 0 and len(temp_sequence) > len(consecutive_sequences):
                    flag = True
                    consecutive_sequences = temp_sequence
                    start, end = i, j
        del nodes[start:end]
        if not flag:
            break
    while nodes.count(0) != 0:
        nodes.remove(0)
    result = ListNode()
    p = result
    for i in nodes:
        p.next = ListNode(i)
        p = p.next
    return result.next

# version 2 - Hash Table
