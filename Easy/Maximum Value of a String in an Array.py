# Difference between isdigit() and isnumeric()

# version 1 - Faster
def maximumValue(strs: list[str]) -> int:
    maximum_value = 0
    for i in range(len(strs)):
        item = strs[i]
        if item.isnumeric(): maximum_value = max(maximum_value, int(item))
        else: maximum_value = max(maximum_value, len(item))
    return maximum_value

# version 2
def maximumValue1(strs: list[str]) -> int:
    max_ = 0
    for ch in strs:
        if ch.isdigit(): 
            print(ch)
            max_ = max(max_, int(ch))
        else: max_ = max(max_, len(ch))
    return max_

strs = ["alic3","bob","3","4","00000"]
print(f"Output: {maximumValue1(strs)}")