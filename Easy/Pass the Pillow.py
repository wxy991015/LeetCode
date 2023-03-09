def passThePillow(n: int, time: int) -> int:
    oneRound = (n - 1) * 2
    res = 0
    remain = time % oneRound
    if remain <= oneRound // 2:
        res = 1 + remain
    else:
        res = n - (remain - oneRound // 2)
    return res

n = 3
time = 2
print(f"Output: {passThePillow(n, time)}")