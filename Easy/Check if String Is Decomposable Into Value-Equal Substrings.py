from typing import List

def isDecomposable(s: str) -> bool:
    if len(s) < 5:
        return False
    stack = [s[0]]
    count = 0
    for i in range(1, len(s)):
        if s[i] == stack[-1]:
            stack.append(s[i])
        else:
            if len(stack) == 2:
                count += 1
            elif len(stack) == 3:
                stack = [s[i]]
            else:
                if (len(stack) - 2) % 3 == 0:
                    count += 1
                    stack = [s[i]]
                else:
                    return False
            if count > 1:
                return False
    if len(stack) == 2:
        return count == 0
    if len(stack) < 3:
        return False
    else:
        if count == 1 and len(stack) % 3 == 0:
            return True
        if count == 1:
            return False
        else:
            if (len(stack) - 2) % 3 != 0:
                return False
    
    if count == 0:
        return False
    return True

s = "011100022233"
print(f"Output: {isDecomposable(s)}")