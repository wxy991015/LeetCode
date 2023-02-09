from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                temp = [nums[i], nums[j], nums[k]]
                temp = sorted(temp)
                if sum(temp) == 0 and temp not in result:
                    result.append(temp)
    return result

nums = [-1,0,1,2,-1,-4]
print(f"Output: {threeSum(nums)}")