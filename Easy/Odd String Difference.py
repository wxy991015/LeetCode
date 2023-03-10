from typing import List

def oddString(words: List[str]) -> str:
    differenceArrays = []
    for i in range(len(words)):
        word = words[i]
        difference = []
        for j in range(1, len(word)):
            difference.append(ord(word[j])-ord(word[j-1]))
        if not difference in differenceArrays:
            if len(differenceArrays) <= 1:
                differenceArrays.append(difference)
            else:
                if difference == differenceArrays[0]:
                    return di
           

words = ["aaa","bob","ccc","ddd"]
print(f"Output: {oddString(words)}")