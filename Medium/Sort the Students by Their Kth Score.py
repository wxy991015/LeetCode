from typing import List
from operator import itemgetter

def sortTheStudents(score: List[List[int]], k: int) -> List[List[int]]:
    score.sort(key=itemgetter(k), reverse=True)
    return score

score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
print(f"Output: {sortTheStudents(score, k)}")