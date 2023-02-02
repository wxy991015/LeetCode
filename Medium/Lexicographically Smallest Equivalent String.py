def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    smallest_equivalent_string = ""
    equivalent_record = dict()
    for i in range(len(s1)):
        if s1[i] in equivalent_record:
            equivalent_record[s1[i]].add(s1[i])
            equivalent_record[s2[i]].add(s2[i])
        else:
            equivalent_record[s1[i]] = set()
    for i in range(len(baseStr)):
        current_str = baseStr[i]
        # continue
    return smallest_equivalent_string