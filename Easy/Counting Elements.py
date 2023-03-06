from typing import List

def countElements(arr: List[int]) -> int:
    arrBucket = [0] * 1001
    for i in range(len(arr)):
        arrBucket[arr[i]] += 1
    res = 0
    for i in range(len(arrBucket)-1):
        if arrBucket[i+1] != 0:
            res += arrBucket[i]
    return res

arr = [1,1,3,3,5,5,7,7]
print(f"Output: {countElements(arr)}")