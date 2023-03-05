from typing import List

# version 1 - brute force
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

# version 2 - binary search
def twoSumLessThanK1(nums: List[int], k: int) -> int:
    nums.sort()
    res = -1
    i, j = 0, len(nums) - 1
    while i < j:
        val = nums[i] + nums[j]
        if val >= k:
            j -= 1
        elif val < k:
            res = max(res, val)
            i += 1
    return res 

nums = [34,23,1,24,75,33,54,8]
k = 60
print(f"Output: {twoSumLessThanK1(nums, k)}")