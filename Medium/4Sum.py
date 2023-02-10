from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
    return result