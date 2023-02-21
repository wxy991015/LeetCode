from typing import List

def maximumGroups(grades: List[int]) -> int:
    if len(grades) == 1:
        return 1
    grades.sort()
    print(grades)
    res = 1
    end = len(grades) - 2
    currSum, currNum = grades[-1], 1
    gradesSum, groupNum = 0, 0
    while end >= 0:
        if gradesSum <= currSum:
            gradesSum += grades[end]
            groupNum += 1
        else:
            if groupNum > currNum:
                res += 1
                currSum, currNum = gradesSum, groupNum
            gradesSum, groupNum = grades[end], 1
        end -= 1
    if gradesSum > currSum and groupNum > currNum:
        res += 1
    return res

grades = [10,6,12,7,3,5]
print(f"Output: {maximumGroups(grades)}")