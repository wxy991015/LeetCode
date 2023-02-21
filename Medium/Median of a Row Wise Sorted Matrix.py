from typing import List

def matrixMedian(grid: List[List[int]]) -> int:
    nums = []
    for i in grid:
        nums.extend(i)
    nums.sort()
    return nums[len(nums)//2]

grid = [[1,1,3,3,4]]
print(f"Output: {matrixMedian(grid)}")