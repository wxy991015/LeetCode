from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    if len(nums) == 1:
        if nums[0] <= 0:
            return 1
        elif nums[0] == 1:
            return 2
        else:
            return 1
    sorted_nums = sorted(list(set(nums)))
    result = 0
    record = 1
    for i in range(len(sorted_nums)):
        if sorted_nums[i] <= 0:
            continue
        if sorted_nums[i] != record:
            result = record
            break
        record += 1
    if result == 0:
        if sorted_nums[-1] <= 0:
            result = 1
        else:
            result = sorted_nums[-1] + 1
    return result

nums = [7,8,9,11,12]
print(f"Output: {firstMissingPositive(nums)}")