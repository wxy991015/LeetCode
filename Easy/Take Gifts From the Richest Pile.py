from typing import List
import math

def pickGifts(gifts: List[int], k: int) -> int:
    while k != 0:
        currMax = max(gifts)
        gifts[gifts.index(currMax)] = int(math.sqrt(currMax))
        k -= 1
    return sum(gifts)

gifts = [1,1,1,1]
k = 4
print(f"Output: {pickGifts(gifts, k)}")