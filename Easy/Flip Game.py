from typing import List

def generatePossibleNextMoves(currentState: str) -> List[str]:
    size = len(currentState)
    res = []
    if size == 1:
        return res
    currentList = list(currentState)
    for i in range(size-1):
        if currentList[i] == "+" and currentList[i+1] == "+":
            currentList[i] = "-"
            currentList[i+1] = "-"
            res.append("".join(currentList))
        currentList = list(currentState)
    return res

currentState = "++++"
print(f"Output: {generatePossibleNextMoves(currentState)}")
    