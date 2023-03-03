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

n = 25
print(f"Output: {alternateDigitSum(n)}")