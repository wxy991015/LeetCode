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

s = "night"
t = "thing"
print(f"Output: {minSteps(s, t)}")