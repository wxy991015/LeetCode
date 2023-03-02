from typing import List

def separateDigits(nums: List[int]) -> List[int]:
    def getDigits(num: int) -> List[int]:
        res = []
        while num // 10 != 0:
            res.append(num%10)
            num //= 10
        res.append(num)
        res.reverse()
        return res
    res = []
    for i in range(len(nums)):
        res.extend(getDigits(nums[i]))
    return res

nums = [32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99]
print(f"Output: {separateDigits(nums)}")
        