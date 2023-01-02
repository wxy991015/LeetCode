"""
First Version
def removeVowels(self, s: str) -> str:
    s = s.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    return s
"""

# Updated Version
def removeVowels(s: str) -> str:
    s_list = [i for i in s if i not in "aeiou"]
    result = "".join(s_list)
    return result

s = "leetcodeisacommunityforcoders"
print(f"Output: {removeVowels(s)}")