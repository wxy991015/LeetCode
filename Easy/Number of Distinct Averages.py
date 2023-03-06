from typing import List

def distinctAverages(nums: List[int]) -> int:
    distinctAvg = set()
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        currMin = nums[i]
        currMax = nums[j]
        avg = (currMax + currMin) / 2
        distinctAvg.add(avg)
        i += 1
        j -= 1
    return len(distinctAvg)

