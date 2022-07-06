def gcd(a, b):
    """Returns the gcd of two numbers a and b, with a>b"""
    assert int(a) == a and int(b) == b, "The numbers must be integers only!"
    if a<0:
        a = -1*a
    if b < 0 :
        b = -1 *b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
print(gcd(48, 18.8))
