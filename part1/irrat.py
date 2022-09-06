"""
    
    Rational numbers are fractions of integer numbers e.g 1/2, -22/7

    Any real number with a finite number of digits after the decimal point is also a rational number e.g 0.45, 8.3/4 = 83/40, 8.3/1.4

    The Fraction Class
    Rational numbers can be represented in python using the Fraction class in the fractions module

    Fractions are automatically reduced:
        Fraction(6, 10) - > Fraction(3, 5)

"""
from fractions import Fraction
import math 
x = Fraction(math.pi) #irrational
y = Fraction(math.sqrt(2))

"""
print(x)
print(float(x))
print(float(y))
print(y)
print(x.limit_denominator(10))
print(x.limit_denominator(100))
"""

a = 0.3
print(a)
print(Fraction(a))
print(format(55, 'b'))
print(format(.55, '.25f'))
print(format(a, '0.5f'))
print(format(a, '0.25f'))

a = Fraction(a)
print(a.limit_denominator(10))

