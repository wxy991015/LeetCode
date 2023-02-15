def reverseParentheses(s: str) -> str:
    res = ""
    open = []
    for i in range(len(s)):
        if s[i] == "(":
            open.append(i)
        elif s[i] == ")":
            sub = s[open[-1]+1:i]
            sub = sub[::-1]
            open.pop()
            res += sub
    return res

s = "(u(love)i)"
print(f"Output: {reverseParentheses(s)}")