def wateringPlants(plants: list[int], capacity: int) -> int:
    steps = 0
    capacity_copy = capacity
    i = 0
    while i < len(plants):
        if capacity >= plants[i]:
            capacity -= plants[i]
            steps += 1
            i += 1
        else:
            capacity = capacity_copy
            steps += i * 2
    return steps

plants = [7,7,7,7,7,7,7]
capacity = 8
print(f"Output: {wateringPlants(plants, capacity)}")

# plants = [1,1,1,4,2,3]