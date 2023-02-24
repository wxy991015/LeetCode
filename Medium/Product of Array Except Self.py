from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    left = [1]
    right = [nums[-1]]
    res = []
    i, j = 1, len(nums) - 2
    while i < len(nums):
        left.append(nums[i]*left[i-1])
        i += 1
    while j >= 0:
        # modify
        right.append(nums[j]*right[i-1])
        j -= 1
    print()
    for i in range(len(nums)):
        product = left[i] * right[len(nums)-i-1]
        res.append(product)
    return res

nums = [1,2,3,4]
print(f"Output: {productExceptSelf(nums)}")