from typing import List
import math

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

# version 2 - hashmap
def unequalTriplets1(nums: List[int]) -> int:
    numsDict = dict()
    for i in range(len(nums)):
        numsDict[nums[i]] = numsDict.get(nums[i], 0) + 1
    size = len(numsDict)
    if size < 3:
        return 0
    res = math.factorial(len(numsDict)) // (math.factorial(3) * math.factorial(len(numsDict)-3))
    for key in numsDict:
        res *= numsDict[key]
    return res

nums = [4,4,2,4,3]
print(f"Output: {unequalTriplets1(nums)}")