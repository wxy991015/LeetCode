from typing import List

def dietPlanPerformance(calories: List[int], k: int, lower: int, upper: int) -> int:
    size = len(calories)
    currSum, currStart = 0, 0
    currCount = 0
    res = 0
    i = 0
    while i < size - 1:
        if currCount != k:
            currSum += calories[i]
            currCount += 1
            print(currSum)
        if currCount == k:
            if currSum < lower:
                res -= 1
            elif currSum > upper:
                res += 1
            currSum -= calories[currStart]
            currCount -= 1
            currStart += 1
        i += 1
    currSum += calories[i]
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