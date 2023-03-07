from typing import List

def mostVisited(n: int, rounds: List[int]) -> List[int]:
    visitedSectors = [0] * n
    for i in range(1, len(rounds)):
        start = rounds[i-1]
        end = rounds[i]
        if start < end:
            for j in range(start, end):
                visitedSectors[j-1] += 1
        else:
            # modify code here 3, 1 -> 3 -> 4 -> 1
            for j in range(start, end, -1):
                visitedSectors[j-1] += 1
    print(visitedSectors)
    res = [1]
    for i in range(1, len(visitedSectors)):
        if visitedSectors[i] == visitedSectors[res[0]]:
            res.append(i+1)
        elif visitedSectors[i] > visitedSectors[res[0]]:
            res = [i+1]
    return res


n = 4
rounds = [1,3,1,2]
print(f"Output: {mostVisited(n, rounds)}")  