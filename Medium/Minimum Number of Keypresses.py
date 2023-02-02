def minimumKeypresses(s: str) -> int:
    minimum_keypresses = 0
    c_record = dict()
    for i in range(len(s)):
        if s[i] in c_record:
            c_record[s[i]] += 1
        else:
            c_record[s[i]] = 1
    sorted_record = dict(sorted(c_record.items(), key=lambda x: x[1], reverse=True))
    start, c_count = 1, 0
    for key in sorted_record:
        if c_count == 9:
            start += 1
            c_count = 0
        c_count += 1
        minimum_keypresses += sorted_record[key] * start
    return minimum_keypresses

s = "aaaaaaaabcdefgggghijkllllllllllmmmnoppponono"
print(f"Output: {minimumKeypresses(s)}")