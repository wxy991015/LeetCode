import collections

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key][1] += 1
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache[key][1] += 1
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = [value, 1]
            else:
                frequency = 1
                invalidate_key = -1
                for k in self.cache:
                    if k[1] >= frequency:
                        frequency = k[1]
                        invalidate_key = k
                self.cache.pop(invalidate_key)
                self.cache[key] = [value, 1]