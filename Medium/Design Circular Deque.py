class MyCircularDeque:
    def __init__(self, k: int):
        self.maxSize = k
        self.queue = []

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.maxSize:
            self.queue.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.maxSize:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop(-1)
            return True
        return False

    def getFront(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if len(self.queue) > 0:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.maxSize