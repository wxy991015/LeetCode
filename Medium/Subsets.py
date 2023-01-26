from typing import List

# version 1 - use list comprehension
def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for i in nums:
        result += [lst + [i] for lst in result]
    return result

# version 2 - use backtrack
