def isStrobogrammatic(num: str) -> bool:
    digits = list(num)
    for i in range(len(num)):
        if digits[i] == "2" or digits[i] == "3" or digits[i] == "4" or digits[i] == "5" or digits[i] == "7":
            return False
        else:
            if digits[i] == "9":
                digits[i] = "6"
            elif digits[i] == "6":
                digits[i] = "9"
    digits.reverse()
    numAfterRotation = "".join(digits)
    return numAfterRotation == num

num = "962"
print(f"Output: {isStrobogrammatic(num)}")