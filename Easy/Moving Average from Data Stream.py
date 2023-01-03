class MovingAverage:
    moving_size = []
    start = 0
    def __init__(self, size: int):
        self.moving_size = [0] * size

    def next(self, val: int) -> float:
        if self.start == len(self.moving_size):
            self.moving_size.pop(0)
            self.moving_size.append(val)
            return sum(self.moving_size) / self.start
        self.moving_size[self.start] = val
        self.start += 1
        print(self.moving_size)
        return sum(self.moving_size) / self.start