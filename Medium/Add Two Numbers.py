from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    p = result
    l1_num, l2_num = [], []
    while l1:
        l1_num.append(l1.val)
        l1 = l1.next
    while l2:
        l2_num.append(l2.val)
        l2 = l2.next
    result_num = [0] * (max(len(l1_num), len(l2_num)) + 1)
    current = 0
    while current < len(l1_num) and current < len(l2_num):
        val = l1_num[current] + l2_num[current]
        if val < 10:
            result_num[current] += val
            if result_num[current] >= 10:
                result_num[current] -= 10
                result_num[current+1] += 1
        else:
            result_num[current] += val - 10
            result_num[current+1] += 1
        current += 1
    if current < len(l1_num):
        while current < len(l1_num):
            val = result_num[current] + l1_num[current]
            if val < 10:
                result_num[current] = val
            else:
                result_num[current] = val - 10
                result_num[current+1] += 1
            current += 1
    if current < len(l2_num):
        while current < len(l2_num):
            val = result_num[current] + l2_num[current]
            if val < 10:
                result_num[current] = val
            else:
                result_num[current] = val - 10
                result_num[current+1] += 1
            current += 1
    if result_num[-1] == 0:
        result_num.pop()
    for i in result_num:
        p.next = ListNode(i)
        p = p.next
    return result.next