from typing import List

def isConvex(points: List[List[int]]) -> bool:
    x_axis = []
    y_axis = []
    for i in range(len(points)):
        x_axis.append(points[i][0])
        y_axis.append(points[i][1])
    min_x, max_x = min(x_axis), max(x_axis)
    min_y, max_y = min(y_axis), max(y_axis)
    for i in range(len(x_axis)):
        if x_axis[i] != min_x and x_axis[i] != max_x and y_axis[i] != min_y and y_axis[i] != max_y:
            return False
    return True

points = [[0,0],[0,5],[5,5],[5,0]]
print(f"Output: {isConvex(points)}")