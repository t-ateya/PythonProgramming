
from cmath import sqrt


def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print("decorated function called: a={0}, b={1}".format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec 

@my_dec(10, 20)
def my_func(s):
    print("Hello {0}".format(s))

#my_func("World")

class MyClass:
    def __init__(self, a, b) -> None:
        self.a = a 
        self.b = b 

    def __call__(self, fn):
        #print("called a = {0}, b= {1}, c={2}".format(self.a, self.b, c))
        def inner(*args, **kwargs):
            print("decorated function called: a={0}, b={1}".format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

@MyClass(10, 20)
def my_func(s):
    print("Hello {0}".format(s))

#my_func("world")


"""
obj = MyClass(10, 20)
obj.__call__(100)
obj(50)
"""

def complete_ordering(cls):
    if "__eq__" in dir(cls) and "__lt__" in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other 
        cls.__gt__ = lambda self, other : not (self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)

    return cls 


@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y **2)

    def __repr__(self) -> str:
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y 
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __le__(self, other):
        pass 

    def __gt__(self, other):
        pass 

    def __ge__(self, other):
        pass 

    def __ne__(self, other):
        pass 


"""
    a <= b iff a < b or a == b
    a > b iff not(a<b) and a != b
    a >= b iff not (a<b)
"""





# ===================================================================================

from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y **2)

    def __repr__(self) -> str:
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y 
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Point):
            return abs(self) > abs(other)
        else:
            return NotImplemented



