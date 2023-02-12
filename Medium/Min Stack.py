from collections import deque

# version 1 - use list stack
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

# version 2 - update stack method
class MinStack:
    def __init__(self):
        self.stack = []

    # push and note the current min value
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        current_min = self.stack[-1][1]
        self.stack.append((val, min(current_min, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]