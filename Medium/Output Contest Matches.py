def findContestMatch(n: int) -> str:
    result_paring = ""
    round = n // 2
    pairing_record = []
    i, j = 1, n
    while i < j:
        pairing_record.append((i, j))
        i += 1
        j -= 1
    print(pairing_record)
    for i in range(2, round):
        temp_record = []
        s, t = 0, len(pairing_record) - 1
        while s < t:
            temp = (pairing_record[s], pairing_record[t])
            temp_record.append(temp)
            s += 1
            t -= 1
        pairing_record = temp_record
    print(pairing_record)
    return result_paring

n = 16
print(f"Output: {findContestMatch(n)}")