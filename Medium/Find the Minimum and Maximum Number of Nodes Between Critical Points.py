from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodesBetweenCriticalPoints(head: Optional[ListNode]) -> list[int]:
    result = [-1, -1]
    critical_points = []
    current = head
    p = current.next
    index = 1
    while p.next:
        if (current.val < p.val and p.next.val < p.val) or (current.val > p.val and p.next.val > p.val):
            critical_points.append(index)
        index += 1
        current = current.next
        p = p.next
    if len(critical_points) < 2:
        return result
    minDistance = critical_points[1] - critical_points[0]
    maxDistance = critical_points[-1] - critical_points[0]
    print(critical_points)
    for i in range(2, len(critical_points)):
        if critical_points[i] - critical_points[i-1] < minDistance:
            minDistance = critical_points[i] - critical_points[i-1]
    return [minDistance, maxDistance]