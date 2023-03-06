from typing import List

def isConsecutive(nums: List[int]) -> bool:
    size = len(nums)
    if size == 1:
        return True
    numsBucket = [0] * (max(size, max(nums)) + 1)
    start = min(nums)
    for i in range(size):
        numsBucket[nums[i]-start] += 1
    for i in range(size):
        if numsBucket[i] == 0:
            return False
    return True

nums = [3,5,4]
print(f"Output: {isConsecutive(nums)}")