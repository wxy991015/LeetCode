from typing import List

# version 1 - triple loop
def unequalTriplets(nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] != nums[j]:
                for k in range(j+1, len(nums)):
                    if nums[i] != nums[k] and nums[j] != nums[k]:
                        res += 1
    return res

nums = [1,1,1,1,1]
print(f"Output: {unequalTriplets(nums)}")