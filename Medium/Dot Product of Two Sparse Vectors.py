from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        for i in range(len(self.nums)):
            dot_product += self.nums[i] * vec.nums[i]
        return dot_product