from typing import List

# version 1 - list comprehension (faster)
def maximumCount(nums: List[int]) -> int:
    pos = [i for i in nums if i > 0]
    neg = [i for i in nums if i < 0]
    return max(len(pos), len(neg))

# version 2 - single loop
def maximumCount1(nums: List[int]) -> int:
    pos = neg = 0
    for i in nums:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
    return max(pos, neg)

nums = [-2,-1,-1,1,2,3, 4]
print(f"Output: {maximumCount1(nums)}")