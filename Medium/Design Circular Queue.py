class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.circularQueue = []

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.circularQueue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            # FIFO => First In First Out
            self.circularQueue.pop(0)
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.circularQueue[0]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.circularQueue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.circularQueue) == 0

    def isFull(self) -> bool:
        return len(self.circularQueue) == self.size