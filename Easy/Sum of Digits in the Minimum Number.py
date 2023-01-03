# version 1 - Faster
def sumOfDigits(nums: list[int]) -> int:
    odd_even, digit_sum = 0, 0
    min_num = min(nums)
    while min_num:
        digit = min_num % 10
        digit_sum += digit
        min_num //= 10
    if digit_sum % 2 == 0:
        odd_even = 1
    return odd_even

# version 2
def sumOfDigits1(nums: list[int]) -> int:
    odd_even, digit_sum = 0, 0
    min_num = min(nums)
    for i in str(min_num):
        digit_sum += int(i)
    if digit_sum % 2 == 0:
        odd_even = 1
    return odd_even

nums = [99,77,33,66,55]
print(f"Output: {sumOfDigits1(nums)}")