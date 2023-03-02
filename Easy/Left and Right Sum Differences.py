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

# version 2
def leftRigthDifference1(nums: List[int]) -> List[int]:
    size = len(nums)
    leftSum = [0] * size
    rightSum = [0] * size
    res = [0] * size
    currLeftSum, currRightSum = 0, 0
    for i in range(size):
        leftSum[i] = currLeftSum
        currLeftSum += nums[i]
    for i in range(size-1, -1, -1):
        rightSum[size-i-1] = currRightSum
        currRightSum += nums[i]
    for i in range(size):
        res[i] = abs(leftSum[i]-rightSum[size-i-1])
    return res

nums = [10,4,8,3]
print(f"Output: {leftRigthDifference1(nums)}")