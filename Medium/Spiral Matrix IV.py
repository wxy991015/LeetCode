from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
    generated_matrix = []
    return generated_matrix