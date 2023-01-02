def rearrangeArray(nums: list[int]) -> list[int]:
    modified_array = []
    positives = [i for i in nums if i > 0]
    negatives = [i for i in nums if i < 0]
    round = len(nums) // 2
    for i in range(round):
        modified_array.append(positives[i])
        modified_array.append(negatives[i])
    return modified_array

nums = [3,1,-2,-5,2,-4]
print(f"Output: {rearrangeArray(nums)}")