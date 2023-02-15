from typing import List

# version 1: double loop
def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals
    sorted_intervals = sorted(intervals)
    res = []
    i = 0
    while i < len(sorted_intervals):
        current = sorted_intervals[i]
        end_point = [current[1]]
        j = i + 1
        while j < len(sorted_intervals) and current[0] <= sorted_intervals[j][0] <= current[1]:
            end_point.append(sorted_intervals[j][1])
            j += 1
            current = [current[0], max(end_point)]
        res.append([current[0], max(end_point)])
        i = j
    return res

# version 2: update sort & loop
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = [intervals[0]]
    for start, end in intervals:
        last = res[-1][1]
        if start <= last:
            res[-1][1] = max(last, end)
        else:
            res.append([start,end])
    return res

intervals = [[1,4],[5,6]]
print(f"Output: {merge(intervals)}")