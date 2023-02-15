from typing import List

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

intervals = [[1,4],[5,6]]
print(f"Output: {merge(intervals)}")