def reverse(n:int)->int:
    """Reverses an integer"""
    x, result = abs(n), 0
    while x:
        remainder = x%10
        result = result*10 + remainder
        x //= 10
    return -result if n < 0 else result

print(reverse(-5619))

