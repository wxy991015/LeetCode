from typing import List

def closetTarget(words: List[str], target: str, startIndex: int) -> int:
    if not target in words:
        return -1
    prev, after = 0, 0
    prevStart, afterStart = startIndex, startIndex
    size = len(words)
    while True:
        if words[afterStart] == target:
            break
        afterStart = (afterStart + 1) % size
        after += 1
    while True:
        if words[prevStart] == target:
            break
        prevStart = (prevStart - 1 + size) % size
        prev += 1
    return min(prev, after)

words = ["i","eat","leetcode"]
target = "ate"
startIndex = 0
print(f"Output: {closetTarget(words, target, startIndex)}")