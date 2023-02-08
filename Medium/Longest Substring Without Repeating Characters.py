# version 1 - stack
def lengthOfLongestSubstring(s: str) -> int:
    max_length = 1
    stack = []
    for i in range(len(s)):
        if s[i] not in stack:
            stack.append(s[i])
        else:
            if len(stack) > max_length:
                max_length = len(stack)
            while s[i] in stack:
                stack.pop(0)
            stack.append(s[i])
    if len(stack) > max_length:
        max_length = len(stack)
    return max_length

# version 2 - sliding window (set)
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r-l+1)
    return res
    
s = "pwwkew"
print(f"Output: {lengthOfLongestSubstring(s)}")