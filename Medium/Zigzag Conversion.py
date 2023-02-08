def convert(s: str, numRows: int) -> str:
    numColumns = len(s) // numRows
    numColumns = numColumns + (numColumns - 1) * (numRows - 2)
    collections = []
    for i in range(numRows):
        collections.append([""] * numColumns)
    print(collections)
    xIndex, yIndex = 0, 0
    i = 0
    while i < len(s):
        if xIndex < numRows:
            collections[xIndex][yIndex] = s[i]
            xIndex += 1
            i += 1
        else:
            xIndex -= 2
            yIndex += 1
            while xIndex > 0:
                print(xIndex, yIndex)
                collections[xIndex][yIndex] = s[i]
                yIndex += 1
                i += 1
                xIndex -= 1
        print(collections)
    result = ""
    for i in range(len(collections)):
        result += "".join(collections[i])
    return result

s = "PAYPALISHIRING"
numRows = 3
print(f"Output: {convert(s, numRows)}")