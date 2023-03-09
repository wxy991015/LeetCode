from typing import List

def hardestWorker(n: int, logs: List[List[int]]) -> int:
    startTime = 0
    maximumRange = -1
    res = 0
    for i in range(len(logs)):
        employeeId, leaveTime = logs[i]
        timeRange = leaveTime - startTime
        if maximumRange == -1:
            res = employeeId
            maximumRange = timeRange
        else:
            if timeRange > maximumRange:
                res = employeeId
                maximumRange = timeRange
            elif timeRange == maximumRange:
                res = min(res, employeeId)
        startTime = leaveTime
    return res

n = 10
logs = [[0,3],[2,5],[0,9],[1,15]]
print(f"Output: {hardestWorker(n, logs)}")