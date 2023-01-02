def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    widest_vertical_area = 0
    fixed_width = [sub[0] for sub in points]
    fixed_width.sort()
    for i in range(1, len(fixed_width)):
        if fixed_width[i] - fixed_width[i-1] > widest_vertical_area:
            widest_vertical_area = fixed_width[i] - fixed_width[i-1]
    return widest_vertical_area

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(f"Output: {maxWidthOfVerticalArea(points)}")