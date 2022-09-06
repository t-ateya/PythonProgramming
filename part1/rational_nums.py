"""
    
    Rational numbers are fractions of integer numbers e.g 1/2, -22/7

    Any real number with a finite number of digits after the decimal point is also a rational number e.g 0.45, 8.3/4 = 83/40, 8.3/1.4

    The Fraction Class
    Rational numbers can be represented in python using the Fraction class in the fractions module

    Fractions are automatically reduced:
        Fraction(6, 10) - > Fraction(3, 5)

"""
from fractions import Fraction

x = Fraction(3, 4)
y = Fraction(22, 7)
z = Fraction(6, -10)
a = Fraction('10')
b = Fraction("0.125")
c = Fraction("22/7")
d = Fraction(2,3)*Fraction(1,2)
e = Fraction(2,3)+Fraction(1,2)
f = Fraction(0.75)
g = Fraction(1.375)


print(x, y, z, a, b, c, d, e, f, g)
print(x.numerator, x.denominator)