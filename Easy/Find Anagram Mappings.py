# version 1 - Faster
def anagramMappings(nums1: list[int], nums2: list[int]) -> list[int]:
    mapping_array = [0] * len(nums1)
    for i in range(len(nums1)):
        mapping_array[i] = nums2.index(nums1[i])
    return mapping_array

# version 2
def anagramMappings(nums1: list[int], nums2: list[int]) -> list[int]:
    mapping_array = []
    for i in nums1:
        mapping_array.append(nums2.index(i))
    return mapping_array

nums1 = [84,46]
nums2 = [84,46]
print(f"Output: {anagramMappings(nums1, nums2)}")