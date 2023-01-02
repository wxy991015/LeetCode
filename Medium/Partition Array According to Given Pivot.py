def pivotArray(nums: list[int], pivot: int) -> list[int]:
    pivot_num = nums.count(pivot)
    partition_nums = [pivot] * pivot_num
    left = []
    nums = [i for i in nums if i != pivot]
    print(nums)
    for i in range(len(nums)):
        if nums[i] > pivot:
            partition_nums.append(nums[i])
        else:
            left.append(nums[i])
    left.extend(partition_nums)
    return left

nums = [9,12,5,10,14,3,10]
pivot = 10
print(f"Output: {pivotArray(nums, pivot)}")