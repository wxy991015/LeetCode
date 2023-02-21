from typing import List

def twoSumLessThanK(nums: List[int], k: int) -> int:
    nums.sort()
    if len(nums) == 1 or nums[0] > k:
        return -1
    print(nums)
    res = 0
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= k / 2:
            high = mid
        else:
            if nums[mid] + nums[mid-1]:
                pass
        

nums = [34,23,1,24,75,33,54,8]
k = 60 
print(f"Output: {twoSumLessThanK(nums, k)}")