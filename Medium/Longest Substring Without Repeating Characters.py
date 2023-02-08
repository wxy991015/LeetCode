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

s = "pwwkew"
print(f"Output: {lengthOfLongestSubstring(s)}")