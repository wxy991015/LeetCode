from typing import List
from collections import Counter

def smallestCommonElement(mat: List[List[int]]) -> int:
    common_elements = [n for (n, cnt) in Counter(num for row in mat for num in row).items() if cnt == len(mat)]
    if len(common_elements) == 0:
        return -1
    return min(common_elements)

mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(f"Output: {smallestCommonElement(mat)}")