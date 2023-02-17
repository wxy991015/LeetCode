from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    while left < right and top < bottom:
        # left to right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1
        if not (left < right and top < bottom):
            break
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1
    return res

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(f"Output: {spiralOrder(matrix)}")
# 1   2  3  4
# 5   6  7  8
# 9  10 11 12
# 13 14 15 16

# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]