from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    strs_copy = []
    for i in range(len(strs)):
        strs_copy.append(sorted(strs[i]))
    anagrams = dict()
    for i in range(len(strs_copy)):
        s = "".join(strs_copy[i])
        if s in anagrams:
            anagrams[s].append(strs[i])
        else:
            anagrams[s] = [strs[i]]
    res = []
    for val in anagrams.values():
        res.append(val)
    return res

strs = ["eat","tea","tan","ate","nat","bat"]
print(f"Output: {groupAnagrams(strs)}")   