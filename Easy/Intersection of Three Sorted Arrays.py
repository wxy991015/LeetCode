# version 1
def arraysIntersection(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    intersection_sorted_array = list(set(arr1) & set(arr2) & set(arr3))
    intersection_sorted_array.sort()
    return intersection_sorted_array

# version 2 - Faster
def arraysIntersection1(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    return sorted(list(set(arr1) & set(arr2) & set(arr3)))

# Question - Why version 2 is faster than version 1

arr1 = [197,418,523,876,1356]
arr2 = [501,880,1593,1710,1870]
arr3 = [521,682,1337,1395,1764]
print(f"Output: {arraysIntersection1(arr1, arr2, arr3)}")