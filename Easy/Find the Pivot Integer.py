def pivotInteger(n: int) -> int:
    pivot_integer = 1
    total = sum(range(1, n+1))
    if n == 1:
        return 1
    else:
        previous_sum = 0
        for i in range(1, n+1):
            if previous_sum != total:
                previous_sum += i
                total -= i - 1
                if previous_sum == total:
                    pivot_integer = i
                    break
        if previous_sum != total:
            pivot_integer = -1
    return pivot_integer

n = 8
print(f"Output: {pivotInteger(n)}")