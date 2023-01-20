from typing import List

def minProductSum(nums1: List[int], nums2: List[int]) -> int:
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted(nums2)
    min_product_sum = 0
    for i in range(len(sorted_nums1)):
        min_product_sum += sorted_nums1[i] * sorted_nums2[len(sorted_nums2)-i-1]
    return min_product_sum

nums1 = [2,1,4,5,7]
nums2 = [3,2,4,8,6]
print(f"Output: {minProductSum(nums1, nums2)}")