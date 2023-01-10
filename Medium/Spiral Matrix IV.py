from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
    res = [[-1 for j in range(n)] for i in range(m)]
    x, y = 0, 0
    dx, dy = 1, 0
    while head:
        res[y][x] = head.val
        if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m or res[y+dy][x+dx] != -1:
            dx, dy = -dy, dx
        x = x + dx
        y = y + dy
        head = head.next
    return res