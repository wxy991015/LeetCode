from typing import List

# version 1 - modulo and string slicing method
def stringShift(s: str, shift: List[List[int]]) -> str:
    def leftShift(s: str, steps: int) -> str:
        while steps != 0:
            s = s[1:] + s[0]
            steps -= 1
        return s
    def rightShift(s: str, steps: int) -> str:
        while steps != 0:
            s = s[-1] + s[:len(s)-1]
            steps -= 1
        return s
    size = len(s)
    for i in range(len(shift)):
        direction, steps = shift[i]
        steps %= size
        if direction == 0:
            s = leftShift(s, steps)
        else:
            s = rightShift(s, steps)
    return s

s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]
print(f"Output: {stringShift(s, shift)}")