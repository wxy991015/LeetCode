from typing import List

def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    result = []
    if len(nums) == 0:
        if upper == lower:
            return [str(lower)]
        return [str(lower) + "->" + str(upper)]
    if lower < nums[0]:
        if nums[0] - lower == 1:
            result.append(str(lower))
        else:
            result.append(str(lower) + "->" + str(nums[0]-1))
    for i in range(len(nums)-1):
        lower_bound, upper_bound = nums[i], nums[i+1]
        difference = upper_bound - lower_bound
        if difference > 1:
            if difference > 2:
                result.append(str(lower_bound+1) + "->" + str(upper_bound-1))
            else:
                result.append(str(lower_bound+1))
    if nums[-1] < upper:
        if upper - nums[-1] == 1:
            result.append(str(upper))
        else:
            result.append(str(nums[-1]+1) + "->" + str(upper))
    return result