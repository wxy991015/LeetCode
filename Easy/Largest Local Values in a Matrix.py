def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    generated_matrix = []
    # get 3*3 grid and find the max value
    for i in range(n-2):
        sub_generated_matrix = []
        for j in range(n-2):
            sub_grid = []
            for k in range(j, j+3):
                for s in range(i, i+3):
                    sub_grid.append(grid[s][k])
            max_value = max(sub_grid)
            sub_generated_matrix.append(max_value)
        generated_matrix.append(sub_generated_matrix)
    return generated_matrix

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(largestLocal(grid))