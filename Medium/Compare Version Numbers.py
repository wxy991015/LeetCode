def compareVersion(version1: str, version2: str) -> int:
    splited_v1 = version1.split(".")
    splited_v2 = version2.split(".")
    size = max(len(splited_v1), len(splited_v2))
    while len(splited_v1) < size:
        splited_v1.append("0")
    while len(splited_v2) < size:
        splited_v2.append("0")
    # print(splited_v1, splited_v2)
    for i in range(size):
        current_v1 = int(splited_v1[i])
        current_v2 = int(splited_v2[i])
        if current_v1 < current_v2:
            return -1
        elif current_v1 > current_v2:
            return 1
    return 0

version1 = "0.1"
version2 = "1.1"
print(f"Output: {compareVersion(version1, version2)}")