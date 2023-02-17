def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    smallest_equivalent_string = ""
    rules = []
    for i in range(len(s1)):
        current_s1 = s1[i]
        current_s2 = s2[i]
        j = 0
        while j < len(rules):
            if current_s1 in rules[j] or current_s2 in rules[j]:
                rules[j].add(current_s1)
                rules[j].add(current_s2)
                break
            j += 1
        if j == len(rules):
            sub_rules = {current_s1, current_s2}
            rules.append(sub_rules)
    print(rules)
    
    for i in range(len(baseStr)):
        current = baseStr[i]
        j = 0
        while j < len(rules):
            if current in rules[j]:
                smallest_equivalent_string += sorted(list(rules[j]))[0]
                break
            j += 1
        if j == len(rules):
            smallest_equivalent_string += current
    return smallest_equivalent_string

s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
print(f"Output: {smallestEquivalentString(s1, s2, baseStr)}")