from typing import List

# version 1 - merge sort
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

# version 2 - dictionary (much faster)
def mergeArrays1(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    mergedNums = dict()
    for i in range(len(nums1)):
        mergedNums[nums1[i][0]] = nums1[i][1]
    for i in range(len(nums2)):
        if nums2[i][0] in mergedNums:
            mergedNums[nums2[i][0]] += nums2[i][1]
        else:
            mergedNums[nums2[i][0]] = nums2[i][1]
    return sorted(list(mergedNums.items()))       

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(f"Output: {mergeArrays1(nums1, nums2)}")