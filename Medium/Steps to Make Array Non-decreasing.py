from typing import List

# version 1 - time limit exceeded
def totalSteps(nums: List[int]) -> int:
    steps = 0
    while True:
        flag = False
        no_increasing_index = []
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                no_increasing_index.append([i, nums[i]])
                flag = True
        for i in range(len(no_increasing_index)):
            nums.pop(no_increasing_index[i][0])
            for j in range(i, len(no_increasing_index)):
                no_increasing_index[j][0] -= 1
        if not flag:
            break
        steps += 1
    return steps

# version 2
def totalSteps(nums: List[int]) -> int:
    st = [[nums[0], 0]]
    # nums = [10,6,5,10,15]
    ans = 0
    for a in nums[1:]:
        t = 0
        while st and st[-1][0] <= a:
            t = max(t, st[-1][1])
            st.pop()
        if st: 
            t += 1
        else:
            t = 0
        ans = max(ans, t)
        st.append([a, t])
    return ans

nums = [10,6,5,10,15]
print(f"Output: {totalSteps(nums)}")