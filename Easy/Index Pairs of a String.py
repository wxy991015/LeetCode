from typing import List

def indexPairs(text: str, words: List[str]) -> List[List[int]]:
    res = []
    for i in range(len(words)):
        word = words[i]
        size = len(word)
        for j in range(len(text)-size+1):
            if text[j:j+size] == word:
                res.append([j,j+size-1])
    return sorted(res)

text = "ababa"
words = ["aba","ab"]
print(f"Output: {indexPairs(text, words)}")