def splitNum(num: int) -> int:
    digits = []
    while num != 0:
        digits.append(num%10)
        num //= 10
    size = len(digits)
    if size == 2:
        return sum(digits)
    digits.sort()
    num1, num2 = digits[0], digits[1]
    for i in range(2, size, 2):
        num1 = num1 * 10 + digits[i]
        print(num1, i)
        if i + 1 < size:
            num2 = num2 * 10 + digits[i+1]
        if i == size - 1:
            break
    return num1 + num2

num = 687
print(f"Output: {splitNum(num)}")
