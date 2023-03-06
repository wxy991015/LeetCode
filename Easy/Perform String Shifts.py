from typing import List

def stringShift(s: str, shift: List[List[int]]) -> str:
    size = len(s)
    listS = list(s)
    for i in range(len(shift)):
        direction, amount = shift[i]
        if direction == 1:
            first = listS[0]
            for j in range(0, size-1):
                listS[j] = listS[j+1]
            listS[-1] = first
        else:
            pass
    