def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1: 
        return 2147483647
    integer_part = abs(dividend) // abs(divisor)
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        integer_part *= -1
    return integer_part

dividend = 7
divisor = -3
print(f"Output: {divide(dividend, divisor)}")