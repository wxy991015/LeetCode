def minPairSum(nums: list[int]) -> int:
    maximum_pair_sum = [0] * (len(nums)//2)
    sorted_nums = sorted(nums)
    i, j = 0, len(nums) - 1
    while i < j:
        maximum_pair_sum[i] = sorted_nums[i] + sorted_nums[j]
        i += 1
        j -= 1
    return max(maximum_pair_sum)

nums = [3,5,4,2,4,6]
print(f"Output: {minPairSum(nums)}")