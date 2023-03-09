from typing import List

def validWordSquare(words: List[str]) -> bool:
    for i in range(len(words)):
        currRow = words[i]
        currCol = ""
        for j in range(len(words[i])):
            if i == len(words[j]):
                currCol += ""
            else:
                currCol += words[j][i]
        if currCol != currRow:
            return False
    return True

words = ["abcd","bnrt","crm","dt"]
print(f"Output: {validWordSquare(words)}")