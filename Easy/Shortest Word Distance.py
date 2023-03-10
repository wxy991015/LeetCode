from typing import List

# nested loop
def shortestDistance(wordsDict: List[str], word1: str, word2: str) -> int:
    res = len(wordsDict)
    words1Occur = []
    words2Occur = []
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            words1Occur.append(i)
        elif wordsDict[i] == word2:
            words2Occur.append(i)
    for i in range(len(words1Occur)):
        for j in range(len(words2Occur)):
            res = min(abs(words1Occur[i]-words2Occur[j]), res)
    return res

# two pointers
def shortestDistance1(wordsDict: List[str], word1: str, word2: str) -> int:
    res = len(wordsDict)
    pos1, pos2 = -1, -1
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            pos1 = i
        elif wordsDict[i] == word2:
            pos2 = i
        if pos1 != -1 and pos2 != -1:
            res = min(res, abs(pos1-pos2))
    return res    

wordsDict = ["practice", "makes", "perfect", "coding", "makes", "makes", "practice", "coding"]
word1 = "makes"
word2 = "coding"
print(f"Output: {shortestDistance1(wordsDict, word1, word2)}")