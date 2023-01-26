from typing import List
from math import gcd

def minimumSplits(nums: List[int]) -> int:
    minimum_subarrays = 0
    start = nums[0]
    i = 1
    while i < len(nums):
        temp_gcd = gcd(start, nums[i])
        if temp_gcd == 1:
            start = nums[i]
            minimum_subarrays += 1
        else:
            start = temp_gcd
        i += 1
    minimum_subarrays += 1
    return minimum_subarrays

nums = [4,12,6,14]
print(f"Output: {minimumSplits(nums)}")