from typing import List

def missingNumber(arr: List[int]) -> int:
    size = len(arr)
    commonDiff = (arr[-1] - arr[0]) // size
    res = arr[0]
    if commonDiff == 0:
        return res
    for i in range(size):
        if arr[i] != res:
            return res
        res += commonDiff
    return -1

arr = [15,13,12]
print(f"Output: {missingNumber(arr)}")