from typing import List

# dictionary "get"
def getCommon(nums1: List[int], nums2: List[int]) -> int:
    nums1Dict = dict()
    for i in range(len(nums1)):
        nums1Dict[nums1[i]] = nums1Dict.get(nums1[i], 0) + 1
    for i in range(len(nums2)):
        if nums1Dict.get(nums2[i], 0) != 0:
            return nums2[i]
    return -1

# merge sort
def getCommon1(nums1: List[int], nums2: List[int]) -> int:
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return -1

nums1 = [1,2,3]
nums2 = [2,4]
print(f"Output: {getCommon1(nums1, nums2)}")