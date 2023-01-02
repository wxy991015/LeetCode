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

# version 2 - 
def countLetters1(s: str) -> int:
    grp = [list(g) for k, g in groupby(s)]
    return sum([len(l) * (len(l) + 1) // 2 for l in grp])
    

s = "aaaaaaaaaa"
print(f"Output: {countLetters1(s)}")