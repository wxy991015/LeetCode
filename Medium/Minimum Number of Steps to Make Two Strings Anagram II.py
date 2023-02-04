from collections import Counter

# version 1 - bucket
def minSteps(s: str, t: str) -> int:
    steps = 0
    s_bucket, t_bucket = [0] * 26, [0] * 26
    for i in s:
        s_bucket[ord(i)-ord("a")] += 1
    for i in t:
        t_bucket[ord(i)-ord("a")] += 1
    for i in range(len(s_bucket)):
        steps += abs(s_bucket[i]-t_bucket[i])
    return steps

# version 2 - Counter
def minSteps(s: str, t: str) -> int:
    steps = 0
    s_counter = Counter(s) # [s[0]: num, s[1]: num, s[2]: num]
    t_counter = Counter(t) # [t[0]: num, t[1]: num, t[2]: num]
    st_counter = (s_counter - t_counter) + (t_counter - s_counter) # find difference both from (s to t) and (t to s)
    for i in st_counter.values():
        steps += i
    return steps

s = "night"
t = "thing"
print(f"Output: {minSteps(s, t)}")