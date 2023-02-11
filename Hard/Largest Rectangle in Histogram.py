from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    largest_rectangle = 0
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            width = j - i + 1
            height = min(heights[i:j+1])
            largest_rectangle = max(largest_rectangle, width * height)
    return largest_rectangle

heights = [2,4]
print(f"Output: {largestRectangleArea(heights)}")