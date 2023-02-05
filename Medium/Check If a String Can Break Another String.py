from typing import List

def checkIfCanBreak(self, s1: str, s2: str) -> bool:
    def permutation(temp: str, s: str, collections: List[int], current: int, steps: int) -> None:
        if current < steps:
            for k in range(len(s)):
                current_str = s[k]
                