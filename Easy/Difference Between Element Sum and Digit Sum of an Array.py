from typing import List

# version 1 - double loop
def differenceOfSum(nums: List[int]) -> int:
    element_sum = sum(nums)
    digits_sum = 0
    for num in nums:
        num = str(num)
        for digit in num:
            digits_sum += int(digit)
    return abs(element_sum - digits_sum)

# version 2 - map method
# map(func, iterables) - operate func for each item in iterables
# work for => string, list, dic, set
# return map object which requires to convert to other iterables
def differenceOfSum1(nums: List[int]) -> int:
    digit_sum = sum(map(int, "".join(map(str, nums))))
    return sum(nums) - digit_sum

nums = [1,15,6,3]
print(f"Output: {differenceOfSum1(nums)}")