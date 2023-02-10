from typing import List

def evalRPN(tokens: List[str]) -> int:
    if len(tokens) == 1:
        return int(tokens[0])
    stack = []
    for i in range(len(tokens)):
        val = tokens[i]
        if len(val) != 1:
            stack.append(val)
        elif val.isnumeric():
            stack.append(val)
        else:
            if val == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first)+int(second))
            elif val == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first)-int(second))
            elif val == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first)*int(second))
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(int(int(first)/int(second)))
    return stack[0]

tokens = ["4","13","5","/","+"]
print(f"Output: {evalRPN(tokens)}")