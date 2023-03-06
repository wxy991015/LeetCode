from typing import List

def largestSubarray(nums: List[int], k: int) -> List[int]:
    size = len(nums)
    if size == k:
        return nums
    if k == 1:
        return [max(nums)]
    currentMax = nums[0]
    res = [nums[0]]
    i = 1
    while i <= size - k:
        if nums[i] < currentMax:
            res.append(nums[i])
        else:
            res = [nums[i]]
        i += 1
    resSize = len(res)
    while resSize != k:
        res.append(nums[i])
        i += 1
        resSize = len(res)
    return res

nums = [1,4,5,2,3]
k = 4
print(f"Output: {largestSubarray(nums, k)}")