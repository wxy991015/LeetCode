from typing import List

def findMaxK(nums: List[int]) -> int:
    nums.sort()
    i = len(nums) - 1
    while i >= 0 and nums[i] > 0:
        if -nums[i] in nums:
            return nums[i]
        i -= 1
    return -1

nums = [-10,8,6,7,-2,-3]
print(f"Output: {findMaxK(nums)}")