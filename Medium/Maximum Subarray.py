from typing import List

def maxSubArray(nums: List[int]) -> int:
    maximum_sum = nums[0]
    prefix_sum = nums[0]
    for i in range(1, len(nums)):
        current = nums[i]
        if prefix_sum < 0:
            prefix_sum = current
        else:
            prefix_sum += current
        maximum_sum = max(prefix_sum, maximum_sum)
    return maximum_sum

nums = [5,4,-1,7,8]
print(f"Output: {maxSubArray(nums)}")