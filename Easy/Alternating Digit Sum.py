def alternateDigitSum(n: int) -> int:
    def splitDigits(n: int):
        digits = []
        while n != 0:
            digits.append(n%10)
            n //= 10
        digits.reverse()
        return digits
    digits = splitDigits(n)
    maxIndex = digits.index(max(digits))
    res = max(digits)
    left, right = maxIndex, maxIndex
    leftFlag, rightFlag = True, True
    while left > 0:
        if leftFlag:
            res -= digits[left-1]
            leftFlag = False
        else:
            res += digits[left-1]
            leftFlag = True
        left -= 1
    while right < len(digits)-1:
        if rightFlag:
            res -= digits[right+1]
            rightFlag = False
        else:
            res += digits[right+1]
            rightFlag = True
        right += 1
    return res

n = 886996
print(f"Output: {alternateDigitSum(n)}")