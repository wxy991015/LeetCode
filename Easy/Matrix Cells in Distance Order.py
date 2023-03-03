from typing import List

def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    def cellDist(cell: List[int], rCenter: int, cCenter: int) -> int:
        return abs(cell[0]-rCenter) + abs(cell[1]-cCenter)
    if rows == 1 and cols == 1:
        return [[rCenter, cCenter]]
    cellDistances = dict()
    for i in range(rows):
        for j in range(cols):
            cell = [i, j]
            cellDistance = cellDist(cell, rCenter, cCenter)
            if cellDistance in cellDistances:
                cellDistances[cellDistance].append(cell)
            else:
                cellDistances[cellDistance] = [cell]
    res = []
    for key in sorted(cellDistances):
        res.extend(cellDistances[key])
    return res

rows = 2
cols = 3
rCenter = 1
cCenter = 2
print(f"Output: {allCellsDistOrder(rows, cols, rCenter, cCenter)}")

"""
...
...
...
...
"""