from typing import List
import collections

# bucket method
def largestUniqueNumber(nums: List[int]) -> int:
    numsBucket = [0] * 1001
    for i in range(len(nums)):
        numsBucket[nums[i]] += 1
    for i in range(1000, -1, -1):
        if numsBucket[i] == 1:
            return i
    return -1

# Counter package
def largestUniqueNumber1(nums: List[int]) -> int:
    return max((v for v, c in collections.Counter(nums).items() if c == 1), default=-1)

nums = [9,9,8,8]
print(f"Output: {largestUniqueNumber1(nums)}")