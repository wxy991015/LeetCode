from typing import List

def oddString(words: List[str]) -> str:
    differences = []
    flag = False
    for i in range(len(words)):
        word = words[i]
        difference = []
        for j in range(1, len(word)):
            d = ord(word[j]) - ord(word[j-1])
            difference.append(d)
        if difference in differences:
            flag = True
        else:
            if flag:
                return word
            else:
                differences.append(difference)
    return ""

words = ["aaa","bob","ccc","ddd"]
print(f"Output: {oddString(words)}")