from typing import List

def dietPlanPerformance(calories: List[int], k: int, lower: int, upper: int) -> int:
    size = len(calories)
    currSum, currStart = 0, 0
    currCount = 0
    res = 0
    for i in range(size-k):
        if currCount != k:
            currSum += calories[i]
            currCount += 1
        if currCount == k:
            if currSum < lower:
                res -= 1
            elif currSum > upper:
                res += 1
            currSum -= calories[currStart] - calories[i+1]
            currStart += 1
    if currSum < lower:
        res -= 1
    elif currSum > upper:
        res += 1
    return res

calories = [6,5,0,0]
k = 2
lower = 1
upper = 5
print(f"Output: {dietPlanPerformance(calories, k, lower, upper)}")