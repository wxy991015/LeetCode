from typing import List

def maxProduct(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    current_max = nums[0]
    current_min = nums[0]
    res = current_max
    for i in range(1, len(nums)):
        current = nums[i]
        temp_max = max(current, current_max * current, current_min * current)
        current_min = min(current, current_max * current, current_min * current)
        current_max = temp_max
        res = max(current_max, res)
    return res

nums = [-2,0,-1]
print(f"Output: {maxProduct(nums)}")