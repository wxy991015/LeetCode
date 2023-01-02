def onesMinusZeros(grid: list[list[int]]) -> list[list[int]]:
    diff = []
    # onesRow => number of ones in a row
    onesRow = [0] * len(grid)

    # zeroesRow => number of zeroes in a row
    zeroesRow = [0] * len(grid)
    for i in range(len(grid)):
        row = grid[i]
        onesRow[i] = row.count(1)
        zeroesRow[i] = row.count(0)
    
    # onesCol => number of ones in a column
    onesCol = [0] * len(grid[0])

    # zeroesCol => number of zeroes in a column
    zeroesCol = [0] * len(grid[0])
    for i in range(len(grid[0])):
        ones = 0
        zeroes = 0
        for j in range(len(grid)):
            if (grid[j][i]) == 1:
                ones += 1
            else:
                zeroes += 1
        onesCol[i] = ones
        zeroesCol[i] = zeroes

    for i in range(len(onesRow)):
        sub_diff = []
        for j in range(len(onesCol)):
            difference = onesRow[i] + onesCol[j] - zeroesRow[i] - zeroesCol[j]
            sub_diff.append(difference)
        diff.append(sub_diff)
    return diff

grid = [[0,1,1],[1,0,1],[0,0,1]]
print(f"Output: {onesMinusZeros(grid)}")