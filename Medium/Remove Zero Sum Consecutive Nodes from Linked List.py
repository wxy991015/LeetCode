from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    p = result
    nums = []
    current = head
    while current:
        nums.append(current)
        current = current.next
    while True:
        flag = False
        if len(nums) > 1:
            for i in range(1, len(nums)):
                if nums[i].val + nums[i-1] == 0:
                    flag = True
                    nums.remove(nums[i-1])
                    nums.remove(nums[i-1])
                    break
        if not flag:
            break
    for i in nums:
        p.next = i
        p = p.next
    return result.next