from typing import List

# version 1
def leftRigthDifference(nums: List[int]) -> List[int]:
    leftSum = []
    rightSum = []
    res = []
    currLeftSum, currRightSum = 0, 0
    for i in range(len(nums)):
        leftSum.append(currLeftSum)
        rightSum.append(currRightSum)
        currLeftSum += nums[i]
        currRightSum += nums[len(nums)-1-i]
    for i in range(len(nums)):
        res.append(abs(leftSum[i]-rightSum[len(nums)-1-i]))
    return res

nums = [10,4,8,3]
print(f"Output: {leftRigthDifference(nums)}")