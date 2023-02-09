# use whole number divisor
def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1: 
        return 2147483647
    integer_part = abs(dividend) // abs(divisor)
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        integer_part *= -1
    return integer_part

# use continuous subtraction
def divide(dividend: int, divisor: int) -> int:
    negatives = 0
    if dividend < 0:
        negatives += 1
        dividend = -dividend
    
    if divisor < 0:
        negatives += 1
        divisor = -divisor
    
    substrations = 0
    while (dividend - divisor >= 0):
        substrations += 1
        dividend -= divisor
    
    if negatives == 1:
        substrations = -substrations
    return substrations

dividend = 7
divisor = -3
print(f"Output: {divide(dividend, divisor)}")