def isMatch(s: str, p: str) -> bool:
    s_bucket = [0] * 26
    p_bucket = [0] * 26
    dot, asterisk = [], []
    for i in range(len(s)):
        s_bucket[ord(s[i])-ord("a")-1] += 1
    for i in range(len(p)):
        if p[i] == ".":
            dot.append(i)
        elif p[i] == "*":
            asterisk.append(i)
        else:
            p_bucket[ord(p[i])-ord("a")-1] += 1
    
    return True