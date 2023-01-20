from typing import List
from collections import Counter

# version 1 - use set intersection method
def longestCommonSubsequence(arrays: List[List[int]]) -> List[int]:
    arrays_set = list(map(set, arrays))
    result = arrays_set[0] & arrays_set[1]
    if len(result) != 0 and len(arrays_set) > 2:
        for i in range(2, len(arrays_set)):
            result = result & arrays_set[i]
    return sorted(list(result))

# version 2 - use Counter from collection package and list comprehension
def longestCommonSubsequence1(arrays: List[List[int]]) -> List[int]:
    return [n for (n, cnt) in Counter(num for arr in arrays for num in arr).items() if cnt == len(arrays)]

arrays = [[1,3,4], [1,4,7,9]]
print(f"Output: {longestCommonSubsequence1(arrays)}")