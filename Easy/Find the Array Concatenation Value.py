from typing import List

def findTheArrayConcVal(nums: List[int]) -> int:
    size = len(nums)
    res = 0
    while size != 0:
        if size == 1:
            res += nums[0]
            nums.pop()
        else:
            res += int(str(nums[0]) + str(nums[-1]))
            nums.pop(-1)
            nums.pop(0)
        size = len(nums)
    return res

nums = [5,14,13,8,12]
print(f"Output: {findTheArrayConcVal(nums)}")