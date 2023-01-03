import pandas as pd

# version 1 - time exceed
def countLetters(s: str) -> int:
    one_distinct_letter_substr = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_string = s[i:j]
            if len(set(sub_string)) == 1:
                one_distinct_letter_substr += 1
    return one_distinct_letter_substr

# version 2 - Faster
def countLetters1(s: str) -> int:
    one_distinct_letter_substr = 0
    i, j = 0, 0
    while i < len(s) and j < len(s):
        while j + 1 < len(s) and s[j] == s[j+1]:
            j += 1
        one_distinct_letter_substr += (1+(j-i+1)) * (j-i+1) // 2
        i = j + 1
        j = i
        """
        if s[j] == s[i]:
            j += 1
        else:
            count = j - i
            one_distinct_letter_substr += (count + 1) * count // 2
            i = j + 1
            j = i
        """
    return one_distinct_letter_substr

s = "aaaaaaaaaa"
print(f"Output: {countLetters1(s)}")