from typing import List

def maxProduct(nums: List[int]) -> int:
    maximum_product = nums[0]
    prefix_product = nums[0]
    for i in range(1, len(nums)):
        current = nums[i]
        if current < 0 and prefix_product < 0:
            prefix_product *= current
        elif current > 0 and prefix_product > 0:
            prefix_product *= current
        else:
            prefix_product = current
        maximum_product = max(prefix_product, maximum_product)
    return maximum_product

nums = [-2,0,-1]
print(f"Output: {maxProduct(nums)}")