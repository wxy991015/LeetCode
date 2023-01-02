def maxIncreaseKeepingSkyline(grid: list[list[int]]) -> int:
    rowLength = len(grid)
    colLength = len(grid[0])
    result = 0
    
    columns = []
    for i in range(rowLength):
        column = []
        for j in range(colLength):
            column.append(grid[j][i])
        columns.append(column)
    
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(columns)):
            column = columns[j]
            result += min(max(row), max(column)) - grid[i][j]
    return result

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(f"Output: {maxIncreaseKeepingSkyline(grid)}")