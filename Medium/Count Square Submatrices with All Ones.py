from typing import List

def countSquares(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    i, side_length = 1, min(m, n)
    result_squares = 0
    while i <= side_length:
        submatrics = []
        temp_side_length, s = i, 0
        while s 
            for t in range(side_length):
                submatrics.append(matrix[s][t])
        if not 0 in submatrics:
            result_squares += 1
        i += 1
    return result_squares
    