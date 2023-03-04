# version 1 - get all the digits
def alternateDigitSum(n: int) -> int:
    def getDigits(n: int):
        digits = []
        while n != 0:
            digits.append(n%10)
            n //= 10
        digits.reverse()
        return digits
    res = 0
    digits = getDigits(n)
    flag = True
    for i in range(len(digits)):
        if flag:
            res += digits[i]
            flag = False
        else:
            res -= digits[i]
            flag = True
    return res

# version 2 - get digits without list
def alternateDigitSum1(n: int) -> int:
    nCopy = n
    digits = 0
    while n != 0:
        digits += 1
        n //= 10
    plus = digits % 2 != 0
    res = 0
    while nCopy != 0:
        digit = nCopy % 10
        if plus:
            res += digit
            plus = False
        else:
            res -= digit
            plus = True
        nCopy //= 10
    return res

n = 25
print(f"Output: {alternateDigitSum1(n)}")