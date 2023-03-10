from collections import Counter

# bucket method
def canPermutePalindrome(s: str) -> bool:
    chrBucket = [0] * 26
    for i in range(len(s)):
        chrBucket[ord(s[i])-ord("a")] += 1
    flag = False
    for i in range(26):
        if chrBucket[i] % 2 == 1:
            if not flag:
                flag = True
            else:
                return False
    return True

# collections.Counter package
def canPermutePalindrome1(s: str) -> bool:
    counts = Counter(s)
    oddCount = 0
    for key in counts:
        if counts[key] % 2 == 1:
            oddCount += 1
            if oddCount > 1:
                return False
    return True

s = "carerac"
print(f"Output: {canPermutePalindrome1(s)}")