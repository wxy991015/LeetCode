from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - Misunderstand the questions
def numComponents(head: Optional[ListNode], nums: list[int]) -> int:
    connected_components = 0
    current = head
    after = current.next
    while after or len(nums) != 0:
        if current.val in nums and after.val in nums:
            connected_components += 1
            nums.remove(current.val)
            nums.remove(after.val)
        current = current.next
        after = after.next
    connected_components += len(nums)
    return connected_components

# version 2 - work but not very fast
def numComponents(head: Optional[ListNode], nums: List[int]) -> int:
    connected_components = 0
    while head:
        if head.val in nums and (head.next == None or head.next.val not in nums):
            connected_components += 1
        head = head.next
    return connected_components