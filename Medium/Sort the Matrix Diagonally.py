import heapq
from typing import DefaultDict

def diagonalSort(mat: list[list[int]]) -> list[list[int]]:
    new_mat = []
    m, n = len(mat), len(mat[0])
    # append diagonal from row
    for i in range(m-1, 0, -1):
        r, c = i, 0
        tmp = []
        while r < m and c < n:
            tmp.append(mat[r][c])
            r += 1
            c += 1
        new_mat.append(sorted(tmp))
    
    # append diagonal from column
    for i in range(n):
        r, c = 0, i
        tmp = []
        while r < m and c < n:
            tmp.append(mat[r][c])
            r += 1
            c += 1
        new_mat.append(sorted(tmp))

    result = []
    for row in range(m):
        i = 0
        tmp = []
        for k in range(len(new_mat)):
            if i >= n: break
            if len(new_mat[k]) == 0: continue
            tmp.append(new_mat[k].pop())
            i += 1
        result.append(tmp)
    result.reverse()
    return result

# version 2 - heap
def diagonalSort1(mat: list[list[int]]) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    new_mat = DefaultDict(list)
    for row in range(m):
        for col in range(n):
            heapq.heappush(new_mat[row-col], mat[row][col])
    print(new_mat.items())
    for row in range(m):
        for col in range(n):
            mat[row][col] = heapq.heappop(new_mat[row-col])
    return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(f"Output: {diagonalSort1(mat)}")