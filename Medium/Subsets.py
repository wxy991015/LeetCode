from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for i in nums:
        result += [lst + [i] for lst in result]
    return result