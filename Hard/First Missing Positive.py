from typing import List

# version 1 - sort
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

# version 2 - single loop
def firstMissingPositive1(nums: List[int]) -> int:
    current = 1
    while current in nums:
        current += 1
    return current

nums = [1,2,0]
print(f"Output: {firstMissingPositive1(nums)}")