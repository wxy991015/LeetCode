def checkArithmeticSubarrays(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    answer = [True] * len(l)
    def isArithmeticSequence(sequence: list[int]):
        delta = sequence[1] - sequence[0]
        for i in range(1, len(sequence)):
            if sequence[i] - sequence[i-1] != delta:
                return False
        return True
    for i in range(len(r)):
        start, end = l[i], r[i]
        sequence = nums[start:end+1]
        sequence.sort()
        if not isArithmeticSequence(sequence):
            answer[i] = False
    return answer

nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
print(f"Output: {checkArithmeticSubarrays(nums, l, r)}")