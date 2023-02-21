from typing import List

# version 1 - brute force
def matrixMedian(grid: List[List[int]]) -> int:
    nums = []
    for i in grid:
        nums.extend(i)
    nums.sort()
    return nums[len(nums)//2]

# version 2 - binary search
def matrixMedian(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    itemsNum = m * n
    l = min(row[0] for row in grid)
    r = max(row[-1] for row in grid)
    print(l, r)
    

grid = [[1,1,3,3,4]]
print(f"Output: {matrixMedian(grid)}")