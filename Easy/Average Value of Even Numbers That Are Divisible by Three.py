from typing import List

def averageValue(nums: List[int]) -> int:
    count = 0
    currentSum = 0
    for i in range(len(nums)):
        if nums[i] % 6 == 0:
            count += 1
            currentSum += nums[i]
    if count == 0:
        return 0
    return int(currentSum/count)

nums = [1,2,4,7,10]
print(f"Output: {averageValue(nums)}")