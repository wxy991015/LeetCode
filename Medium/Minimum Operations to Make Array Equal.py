def minOperations(n: int) -> int:
    operations = 0
    nums = [0] * n
    for i in range(n):
        nums[i] = i * 2 + 1
    middle = nums[n//2]
    if n % 2 == 0:
        middle = (nums[0] + nums[-1]) // 2
    i = 0
    while i < n // 2:
        operations += middle - nums[i]
        i += 1
    return operations

n = 3
print(f"Output: {minOperations(n)}")