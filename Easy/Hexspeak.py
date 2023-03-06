def toHexspeak(num: str) -> str:
    letters = {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}
    hexDecimalStr = hex(int(num)).upper()[2:]
    hexDecimalStr = hexDecimalStr.replace("0", "O").replace("1", "I")
    for i in hexDecimalStr:
        if not i in letters:
            return "ERROR"
    return hexDecimalStr
    
num = "3"
print(f"Output: {toHexspeak(num)}")