from typing import List

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    sorted_intervals = sorted(intervals)
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
            return False
    return True

intervals = [[7,10],[2,4]]
print(f"Output: {canAttendMeetings(intervals)}")