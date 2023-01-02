def minOperations(boxes: str) -> list[int]:
    boxes = list(boxes)
    for i in range(len(boxes)):
        boxes[i] = int(boxes[i])
    answer = [0] * len(boxes)
    for i in range(len(boxes)):
        operations = 0
        for j in range(len(boxes)):
            if boxes[j] == 1:
                operations += abs(j-i)
        answer[i] = operations
    return answer

boxes = "001011"
print(f"Output: {minOperations(boxes)}")