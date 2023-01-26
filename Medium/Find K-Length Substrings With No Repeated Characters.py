def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    if k > len(s):
        return 0
    number_of_substrings = 0
    for i in range(len(s)-k+1):
        substring = s[i:i+k]
        if len(set(substring)) == k:
            number_of_substrings += 1
    return number_of_substrings

s = "home"
k = 5
print(f"Output: {numKLenSubstrNoRepeats(s, k)}")