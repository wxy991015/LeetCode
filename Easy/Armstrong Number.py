import math

# version 1
def isArmstrong(n: int) -> bool:
    str_n = str(n)
    digit_sum = 0
    for i in str_n:
        digit_sum += int(i) ** len(str_n)
    return digit_sum == n

# version 2 - Faster
def isArmstrong1(n: int) -> bool:
    digit_sum = 0
    n_copy = n
    # calculate the digit by using math module
    k = math.floor(math.log10(n)) + 1
    while n_copy:
        digit = n_copy % 10
        digit_sum += digit ** k
        n_copy //= 10
    return digit_sum == n

n = 123
print(f"Output: {isArmstrong1(n)}")