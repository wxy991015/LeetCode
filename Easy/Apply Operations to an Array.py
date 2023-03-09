from typing import List

def applyOperations(nums: List[int]) -> List[int]:
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i] * 2
            nums[i+1] = 0
    zeroCount = nums.count(0)
    res = [i for i in nums if i != 0]
    res.extend(zeroCount * [0])
    return res

nums = [0,1]
print(f"Output: {applyOperations(nums)}")   