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

s = "carerac"
print(f"Output: {canPermutePalindrome(s)}")