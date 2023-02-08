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
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0
    for i in range(len(nums)):
        val = abs(nums[i])
        if 1 <= val <= len(nums):
            if nums[val-1] > 0:
                nums[val-1] *= -1
            elif nums[val-1] == 0:
                nums[val-1] = -1 * (len(nums)+1)
    for i in range(1, len(nums) + 1):
        if nums[i-1] >= 0:
            return i
    return len(nums) + 1

nums = [1,2,0]
print(f"Output: {firstMissingPositive1(nums)}")