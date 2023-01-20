from typing import List

# version 1 - time limit exceeded (list comprehension is slow)
def findBuildings(heights: List[int]) -> List[int]:
    result = []
    result.append(0)
    for i in range(1, len(heights)):
        result = [height for height in result if heights[height] > heights[i]]
        result.append(i)
    return sorted(result)

# version 2 - stack (pop method)
def findBuildings1(heights: List[int]) -> List[int]:
    result_stack = []
    result_stack.append(0)
    for i in range(1, len(heights)):
        if heights[i] >= heights[result_stack[-1]]:
            while len(result_stack) > 0 and heights[result_stack[-1]] <= heights[i]:
                result_stack.pop()
        result_stack.append(i)
    return result_stack


heights = [4,3,2,1]
print(f"Output: {findBuildings1(heights)}")