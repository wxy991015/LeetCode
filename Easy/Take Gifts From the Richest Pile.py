from typing import List
import math
from queue import PriorityQueue
import heapq

# sort & max method
def pickGifts(gifts: List[int], k: int) -> int:
    while k != 0:
        currMax = max(gifts)
        gifts[gifts.index(currMax)] = int(math.sqrt(currMax))
        k -= 1
    return sum(gifts)

# priority queue & heap method
def pickGifts1(gifts: List[int], k: int) -> int:
    heapGifts = [-i for i in gifts]
    heapq.heapify(heapGifts)
    while k != 0:
        currMax = -heapq.heappop(heapGifts)
        currMax = int(math.sqrt(currMax))
        heapq.heappush(heapGifts, -currMax)
        k -= 1
    heapGifts = [-i for i in heapGifts]
    return sum(heapGifts)
    

gifts = [25,64,9,4,100]
k = 4
print(f"Output: {pickGifts1(gifts, k)}")