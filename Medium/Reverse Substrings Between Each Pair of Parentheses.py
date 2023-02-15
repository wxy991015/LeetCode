def reverseParentheses(s: str) -> str:
    s_list = list(s)
    res = ""
    open = []
    for i in range(len(s_list)):
        if s_list[i] == "(":
            open.append(i)
        elif s_list[i] == ")":
            start = open.pop()
            s_list[start:i+1] = s_list[start:i+1][::-1]
    for i in range(len(s_list)):
        if s_list[i] != "(" and s_list[i] != ")":
            res += s_list[i]
    return res

s = "(ed(et(oc))el)"
print(f"Output: {reverseParentheses(s)}")