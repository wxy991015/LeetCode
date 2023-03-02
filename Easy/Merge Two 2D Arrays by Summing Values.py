from typing import List

def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i][0] < nums2[j][0]:
            res.append(nums1[i])
            i += 1
        elif nums1[i][0] > nums2[j][0]:
            res.append(nums2[j])
            j += 1
        else:
            res.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
            i += 1
            j += 1
    while i < len(nums1):
        res.append(nums1[i])
        i += 1
    while j < len(nums2):
        res.append(nums2[j])
        j += 1
    return res

nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
print(f"Output: {mergeArrays(nums1, nums2)}")