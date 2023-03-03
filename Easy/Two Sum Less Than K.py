from typing import List

def twoSumLessThanK(nums: List[int], k: int) -> int:
    nums.sort()
    if len(nums) == 1 or nums[0] + nums[1] >= k:
        return -1
    print(nums)
    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            val = nums[i] + nums[j]
            if val >= k:
                break
            else:
                res = max(res, val)
    return res
        

nums = [10,20,30]
k = 15
print(f"Output: {twoSumLessThanK(nums, k)}")