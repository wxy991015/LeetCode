class ArrayReader:
   def get(self, index: int) -> int:
       pass

def search(reader: 'ArrayReader', target: int) -> int:
    start = 0
    while reader.get(start) <= target:
        if reader.get(start) == target:
            return start
        start += 1
    return -1