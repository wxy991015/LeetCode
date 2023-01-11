class FrontMiddleBackQueue:
    def __init__(self):
        self.fmb = []

    def pushFront(self, val: int) -> None:
        self.fmb.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        middle = len(self.fmb) // 2
        self.fmb.insert(middle, val)

    def pushBack(self, val: int) -> None:
        self.fmb.append(val)

    def popFront(self) -> int:
        if len(self.fmb) == 0:
            return -1
        return self.fmb.pop(0)

    def popMiddle(self) -> int:
        if len(self.fmb) == 0:
            return -1
        middle = len(self.fmb) // 2
        if len(self.fmb) % 2 == 0:
            middle -= 1
        return self.fmb.pop(middle)

    def popBack(self) -> int:
        if len(self.fmb) == 0:
            return -1
        return self.fmb.pop()