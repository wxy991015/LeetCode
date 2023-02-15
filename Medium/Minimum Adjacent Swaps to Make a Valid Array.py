from typing import List

def minimumSwaps(nums: List[int]) -> int:
    swaps_res = 0
    if nums.index(min(nums)) == 0 and nums.index(max(nums)) == len(nums) - 1:
        return 0
    min_val, max_val = min(nums), max(nums)
    start, end = 0, len(nums) - 1
    while nums[start] != min_val:
        start += 1
    while nums[end] != max_val:
        end -= 1
    swaps_res += (len(nums) - end - 1) + start
    if start >= end:
        swaps_res -= 1
    return swaps_res