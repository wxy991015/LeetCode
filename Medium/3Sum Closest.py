from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    if len(nums) == 3:
        return sum(nums)
    closest_nums = []
    upper_bound, lower_bound = target, target
    while len(closest_nums) < 3:
        if upper_bound in nums:
            closest_nums += nums.count(upper_bound) * [upper_bound]
            print(closest_nums)
        if lower_bound != upper_bound and lower_bound in nums:
            closest_nums += nums.count(lower_bound) * [lower_bound]
        upper_bound += 1
        lower_bound -= 1
    print(closest_nums)
    return sum(closest_nums)

nums = [0,0,0]
target = 1
print(f"Output: {threeSumClosest(nums, target)}")