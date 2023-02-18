def calculate(s: str) -> int:
    s = s.strip()
    res = 0
    nums, operations = [], []
    for i in range(len(s)):
        if s[i] == " ":
            continue
        if s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
            operations.append(i)
            if len(operations) == 1:
                nums.append(s[:i])
            else:
                prefix, suffix = operations[-2], operations[-1]
                nums.append(s[prefix+1:suffix].strip())
    nums.append(s[operations[-1]+1:])
    print(nums, operations)
    adds_substraction = []
    return res

s = " 3/2 "
print(f"Output: {calculate(s)}")