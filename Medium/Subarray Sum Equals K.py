from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    res = 0
    currentSum = 0
    prefixSums = {0:1}
    for n in nums:
        currentSum += n
        diff = currentSum - k
        res += prefixSums.get(diff, 0)
        prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)
    return res