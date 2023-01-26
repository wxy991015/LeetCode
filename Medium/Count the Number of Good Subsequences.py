def countGoodSubsequences(s: str) -> int:
    subsequences = []
    def helper(start: int, temp: str) -> int:
        if len(temp) != 0:
            subsequences.append(temp)
        for i in range(start, len(s)):
            helper(i+1, temp + s[start])
    helper(0, "")
    good_subsequences = 0
    for i in range(len(subsequences)):
        subsequnece = subsequences[i]
        if len(subsequnece) % len(set(subsequnece)) == 0:
            good_subsequences += 1
    return good_subsequences % (10 ** 9 + 7)

s = "abcd"
print(f"Output: {countGoodSubsequences(s)}")        