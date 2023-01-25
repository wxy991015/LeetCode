from typing import List

def countMaxOrSubsets(nums: List[int]) -> int:
    temp, result = [], []
    def solver(start: int, temp: List[int], output: List[List[int]]) -> None:
        if len(temp) != 0:
            result.append(temp)
        for i in range(start, len(nums)):
            solver(i+1, temp + [nums[i]], output)
    solver(0, temp, result)
    maximum_bitwise = bitwise_result = 0
    for i in range(len(result)):
        subset = result[i]
        temp_max = subset[0]
        for j in range(1, len(subset)):
            temp_max |= subset[j]
        if temp_max > maximum_bitwise:
            bitwise_result = 1
            maximum_bitwise = temp_max
        elif temp_max == maximum_bitwise:
            bitwise_result += 1
    return bitwise_result
