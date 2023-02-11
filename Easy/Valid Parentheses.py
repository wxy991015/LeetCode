def isValid(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            stack.append(s[i])
        else:
            if i == 0 or len(stack) == 0:
                return False
            elif s[i] == ")" and stack[-1] != "(":
                return False
            elif s[i] == "]" and stack[-1] != "[":
                return False
            elif s[i] == "}" and stack[-1] != "{":
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True

s = "(]"
print(f"Output: {isValid(s)}")