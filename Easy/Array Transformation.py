from typing import List

def transformArray(arr: List[int]) -> List[int]:
    currentArray = arr.copy()
    while True:
        for i in range(1, len(arr)-1):
            if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                arr[i] += 1
            elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                arr[i] -= 1
        if currentArray == arr:
            break
        currentArray = arr.copy()
    return arr

arr = [1,6,3,4,3,5]
print(f"Output: {transformArray(arr)}")