def minMaxDifference(num: int) -> int:
    strMax, strMin = str(num), str(num)
    for i in range(len(strMax)):
        if strMax[i] != "9":
            strMax = strMax.replace(strMax[i], "9")
            break
    for i in range(len(strMin)):
        if strMin[i] != "0":
            strMin = strMin.replace(strMin[i], "0")
            break
    return int(strMax) - int(strMin)

num = 90
print(f"Output: {minMaxDifference(num)}")