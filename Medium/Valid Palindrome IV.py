def makePalindrome(s: str) -> bool:
    operations_count = 0
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            operations_count += 1
        if operations_count > 2:
            return False
        i += 1
        j -= 1
    return True

s = "abcdef"
print(f"Output: {makePalindrome(s)}")