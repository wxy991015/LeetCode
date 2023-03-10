from typing import List

def oddString(words: List[str]) -> str:
    differenceArrays = dict()
    for i in range(len(words)):
        word = words[i]
        difference = []
        for j in range(1, len(word)):
            difference.append(ord(word[j])-ord(word[j-1]))
        difference = tuple(difference)
        if difference in differenceArrays:
            differenceArrays[difference].append(word)
        else:
            differenceArrays[difference] = [word]
    print(differenceArrays.items())
    for key in differenceArrays:
        if len(differenceArrays[key]) == 1:
            return differenceArrays[key][0]
    return ""
           

words = ["aaa","bob","ccc","ddd"]
print(f"Output: {oddString(words)}")