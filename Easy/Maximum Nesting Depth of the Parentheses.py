from collections import deque

# stack (Python deque) method
def maxDepth(s: str) -> int:
    dp = deque()
    res = 0
    for i in range(len(s)):
        if s[i] == "(":
            dp.append(s[i])
        elif s[i] == ")":
            currDepth = len(dp)
            res = max(currDepth, res)
            dp.pop()
    return res

# single loop
def maxDepth1(s: str) -> int:
    currDepth = 0
    res = 0
    for i in range(len(s)):
        if s[i] == "(":
            currDepth += 1
            res = max(currDepth, res)
        elif s[i] == ")":
            currDepth -= 1
    return res

s = "(1)+((2))+(((3)))"
print(f"Output: {maxDepth1(s)}")