def countTime(time: str) -> int:
    res = 1
    if time[0] == "?":
        if time[1] == "?" or time[1] <= "3":
            res *= 3
        else:
            res *= 2
    if time[1] == "?":
        if time[0] <= "1":
            res *= 10
        else:
            if time[0] == "?":
                res = 24
            else:
                res *= 4
    if time[3] == "?":
        res *= 6
    if time[4] == "?":
        res *= 10
    return res

time = "??:??"
print(f"Output: {countTime(time)}")