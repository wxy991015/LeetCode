from typing import List

def fixedPoint(arr: List[int]) -> int:
    l, h = 0, len(arr) - 1
    res = -1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] < mid:
            l = mid + 1
        else:
            if arr[mid] == mid:
                res = mid
            h = mid - 1
    return res

arr = [-10,-5,0,3,7]
print(f"Output: {fixedPoint(arr)}")