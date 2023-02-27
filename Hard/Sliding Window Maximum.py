from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    monoStack = [nums[0]]
    res = []
    for i in range(len(nums)):
        if nums[i] <= monoStack[-1]:
            monoStack.append(nums[i])
        else:
            while len(monoStack) > 0 and nums[i] > monoStack[-1]:
                monoStack.pop()
            monoStack.append(nums[i])
        if i >= k - 1:
            res.append(monoStack[0])
    return res

nums = [1]
k = 1
print(f"Output: {maxSlidingWindow(nums, k)}")