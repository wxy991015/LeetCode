def confusingNumber(n: int) -> bool:
    digits = []
    nCopy = n
    while n != 0:
        digits.append(n%10)
        n //= 10
    for i in range(len(digits)):
        if digits[i] == 2 or digits[i] == 3 or digits[i] == 4 or digits[i] == 5 or digits[i] == 7:
            return False
        else:
            if digits[i] == 6:
                digits[i] = 9
            elif digits[i] == 9:
                digits[i] = 6
    newN = 0
    for i in range(len(digits)):
        newN = newN * 10 + digits[i]
    return newN != nCopy

n = 11
print(f"Output: {confusingNumber(n)}")