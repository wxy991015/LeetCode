from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    def mergeSort(nums1: List[int], nums2: List[int]):
        result = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        return result
    merged_nums = mergeSort(nums1, nums2)
    print(merged_nums)
    if len(merged_nums) == 0:
        return float(0)
    size = len(merged_nums)
    if len(merged_nums) % 2 == 0:
        return (merged_nums[size//2] + merged_nums[size//2-1]) / 2
    return float(merged_nums[size//2])

nums1 = [1,2]
nums2 = [3,4]
print(f"Output: {findMedianSortedArrays(nums1, nums2)}")