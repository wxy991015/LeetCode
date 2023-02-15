from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    while k != 0:
        end = nums.pop()
        nums.insert(0, end)
        k -= 1