from typing import List

def areSentencesSimilar(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    sentence1Size, sentence2Size = len(sentence1), len(sentence2)
    if sentence1Size != sentence2Size:
        return False
    for i in range(sentence1Size):
        currentPair = [sentence1[i], sentence2[i]]
        if not sentence1[i] == sentence2[i] and not currentPair in similarPairs and not list(reversed(currentPair)) in similarPairs:
            return False
    return True

sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
print(f"Output: {areSentencesSimilar(sentence1, sentence2, similarPairs)}")