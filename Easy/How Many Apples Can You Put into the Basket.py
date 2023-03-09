from typing import List

def maxNumberOfApples(weight: List[int]) -> int:
    weight.sort()
    currSum = sum(weight)
    res = len(weight)
    i = -1
    while currSum > 5000:
        currSum -= weight[i]
        res -= 1
        i -= 1
    return res

weight = [900,950,800,1000,700,800]
print(f"Output: {maxNumberOfApples(weight)}")