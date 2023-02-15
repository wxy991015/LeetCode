from typing import List

def findMin(nums: List[int]) -> int:
    nums.sort()
    return nums[0]