def commonFactors(a: int, b: int) -> int:
    common_factors = 0
    min_value = min(a, b)
    max_value = max(a, b)
    for i in range(1, min_value+1):
        if min_value % i == 0 and max_value % i == 0:
            common_factors += 1
    return common_factors

a = 25
b = 30
print(f"Output: {commonFactors(a, b)}")