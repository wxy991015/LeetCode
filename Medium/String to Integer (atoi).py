def myAtoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    num_result = 0
    digits = ""
    sign = 1
    i = 0
    if s[0] == "-":
        sign = -1
        i += 1
    elif s[0] == "+":
        i += 1
    while i < len(s):
        if s[i].isdigit():
            digits += s[i]
        else:
            break
        i += 1
    if len(digits) > 0:
        num_result = int(digits) * sign
    if num_result < -2 ** 31:
        num_result = -2 ** 31
    elif num_result > 2 ** 31 - 1:
        num_result = 2 ** 31 - 1
    return num_result

s = "4193 with words"
print(f"Output: {myAtoi(s)}")