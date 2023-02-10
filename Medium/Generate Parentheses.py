from typing import List

def generateParenthesis(n: int) -> List[str]:
    stack = []
    res = []
    def backTrack(openN: int, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            backTrack(openN+1, closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            backTrack(openN, closeN)
            stack.pop()
    backTrack(0, 0)
    return res