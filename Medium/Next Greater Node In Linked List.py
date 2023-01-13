from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - time limit exceeds
def nextLargerNodes(head: Optional[ListNode]) -> list[int]:
    p = head
    size = 0
    while p:
        size += 1
        p = p.next
    answer = [0] * size
    current = head
    i = 0
    while current:
        temp = current.next
        flag = False
        while temp:
            if temp.val > current.val:
                flag = True
                answer[i] = temp.val
                break
            temp = temp.next
        i += 1
        current = current.next
    return answer

# version 2:
def nextLargerNodes(head: Optional[ListNode]) -> list[int]:
    position = -1
    answer, stack = [], []
    while head:
        position += 1
        answer.append(0)
        while stack and stack[-1][1] < head.val:
            index, value = stack.pop()
            answer[index] = head.val
        stack.append((position, value))
        head = head.next
    return answer