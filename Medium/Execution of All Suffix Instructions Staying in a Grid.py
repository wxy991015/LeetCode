def executeInstructions(n: int, startPos: list[int], s: str) -> list[int]:
    answer = [0] * len(s)
    startPosCopy = startPos.copy()
    # move the robot by instruction
    def move(instruction: str):
        if instruction == "L":
            startPosCopy[1] -= 1
        elif instruction == "R":
            startPosCopy[1] += 1
        elif instruction == "U":
            startPosCopy[0] -= 1
        else:
            startPosCopy[0] += 1
    for i in range(len(s)):
        for j in range(i, len(s)):
            move(s[j])
            x, y = startPosCopy[0], startPosCopy[1]
            if 0 <= x <= n - 1 and 0 <= y <= n - 1:
                answer[i] += 1
            else:
                break
        startPosCopy = startPos.copy()
    return answer

n = 2
startPos = [1,1]
s = "LURD"
print(f"Output: {executeInstructions(n, startPos, s)}")