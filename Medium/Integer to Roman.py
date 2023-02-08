def intToRoman(num: int) -> str:
    roman_result = ""
    while num != 0:
        if num >= 1000:
            roman_result += "M"
            num -= 1000
        elif num >= 900:
            roman_result += "CM"
            num -= 900
        elif num >= 500:
            roman_result += "D"
            num -= 500
        elif num >= 400:
            roman_result += "CD"
            num -= 400
        elif num >= 100:
            roman_result += "C"
            num -= 100
        elif num >= 90:
            roman_result += "XC"
            num -= 90
        elif num >= 50:
            roman_result += "L"
            num -= 50
        elif num >= 40:
            roman_result += "XL"
            num -= 40
        elif num >= 10:
            roman_result += "X"
            num -= 10
        elif num >= 9:
            roman_result += "IX"
            num -= 9
        elif num >= 5:
            roman_result += "V"
            num -= 5
        elif num >= 4:
            roman_result += "IV"
            num -= 4
        else:
            roman_result += "I"
            num -= 1
    return roman_result

num = 1994
print(f"Output: {intToRoman(num)}")
            