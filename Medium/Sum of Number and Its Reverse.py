# version 1 - brute force
def sumOfNumberAndReverse(num: int) -> bool:
    def isReverseNumber(num1: int, num2: int) -> bool:
        if num1 == 0 and num2 == 0:
            return True
        if (num1 == 0 and num2 != 0) or (num1 != 0 and num2 == 0):
            return False
        if ("0" + str(min(num1, num2)) == str(max(num1, num2))[::-1]):
            return True
        return str(num1) == str(num2)[::-1]
    rounds = num // 2
    for i in range(rounds+1):
        num1, num2 = i, num - i
        if isReverseNumber(num1, num2):
            return True
    return False

num = 443
print(f"Output: {sumOfNumberAndReverse(num)}")