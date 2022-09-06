# n = (n//b)*b + n%b wher b is the base and n the number
#Example, represent n =232 in base b = 5

"""
    232 = (232 // 5) *5 + 232%5 = 46*5 + 2
        = [46*5^1] + [2*5^0]
        = [((46 // 5))*5 + 46 % 5)*5^1] + [2*5^0]
        = [(9 * 5 + 1)*5^1] + [2 * 5^0]
        = [((9 // 5) * 5 + 9%5) * 5^2] + [1*5^1] + [2*5^0]
        = [(1 * 5 + 4)* 5^2] + [1 * 5^1] + [2 * 5^0]
        = [1 * 5^3] + [4*5^2] + [1*5^1] + [2*5^0]
"""

def from_base(n, b):
    if b < 2:
        raise ValueError("Base b must be >= 2")
    if n < 0:
        raise ValueError("Number n must be >=0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        #m, n = n%b, n//b 
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits.")
    return "".join([digit_map[d] for d in digits ])

def rebase_from10(number, base):
    digit_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = "-"+encoding
    return encoding

    
"""
print(encode([15, 15], "0123456789ABCDEF"))

#print(from_base(10,2))
#print(from_base(255,16))
"""

e = rebase_from10(-314, 2)
print(e)
print(int(e, base=2))
print(int('FF', base = 16))

print("\n====================")
e = rebase_from10(-3451, 16)
print(e)
print(int(e, base=16))

