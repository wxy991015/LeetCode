# version 1 - time limit exceeded
def differenceByOne(s: str, t: str) -> bool:
    difference = 0
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            difference += 1
            if difference > 1:
                return False
    return difference == 1

def countSubstrings(s: str, t: str) -> int:
    result = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            s_substring = s[i:j]
            for k in range(len(t)):
                for w in range(k+1, len(t)+1):
                    t_substring = t[k:w]
                    if differenceByOne(s_substring, t_substring):
                        result += 1
    return result

s = "ab"
t = "bb"
print(f"Output: {countSubstrings(s, t)}")