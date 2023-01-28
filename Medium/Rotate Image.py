from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    def solver(matrix: List[List[int]], offset: int, n: int) -> None:
        if offset >= n:
            return
        length = len(matrix) - 1
        for i in range(offset, n):
            t = matrix[offset][i]
            matrix[offset][i] = matrix[length-i][offset]
            matrix[length-i][offset] = matrix[length-offset][length-i]
            matrix[length-offset][length-i] = matrix[i][length-offset]
            matrix[i][length-offset] = t
        solver(matrix, offset+1, n-1)
    solver(matrix, 0, n-1)
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)