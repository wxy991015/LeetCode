# version 1
def countDigits(num: int) -> int:
    num_of_digits = 0
    num_copy = num
    while num != 0:
        digit = num % 10
        if num_copy % digit == 0:
            num_of_digits += 1
        num = int(num / 10)
    return num_of_digits

def countDigits1(num: int) -> int:
    num_of_digits = 0
    str_num = str(num)
    for i in str_num:
        if num % int(i) == 0:
            num_of_digits += 1
    return num_of_digits

"""
def countDigits(self, num):
    str_num, count = str(num), 0
    for digit in str_num:
        if num % int(digit) == 0:
            count += 1
    return count
"""

num = 1248
print(f"Output: {countDigits1(num)}")