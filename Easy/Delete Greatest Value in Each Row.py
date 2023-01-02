def deleteGreatestValue(grid: list[list[int]]) -> int:
    final_answer = 0
    while any(grid):
        max_value = []
        for i in range(len(grid)):
            if len(grid[i]) != 0:
                max_value.append(max(grid[i]))
                grid[i].remove(max(grid[i]))
        final_answer += max(max_value)
    return final_answer

grid = [[10]]
print(f"Output: {deleteGreatestValue(grid)}")