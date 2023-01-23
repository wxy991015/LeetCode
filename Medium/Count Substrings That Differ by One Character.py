def differenceByOne(s: str, t: str) -> bool:
    

def countSubstrings(s: str, t: str) -> int:
    result = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            s_substring = s[i:j]
            for k in range(len(t)):
                for w in range(i+1, len(t)+1):
                    t_substring = t[k:w]
                    if len(s_substring) == len(t_substring) and s_substring != t_substring:
                        
                        
    return result