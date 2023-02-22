from typing import List

# version 1 - brute force
def kthSmallest(matrix: List[List[int]], k: int) -> int:
    matrixItems = []
    for i in matrix:
        matrixItems.extend(i)
    matrixItems.sort()
    return matrixItems[k-1]

# version 2 - binary search
