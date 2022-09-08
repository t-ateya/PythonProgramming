
s = [10, 20, 30]

#shallow copy
cp = s.copy()
cp = s[0:len(s)]
cp = s[:]
cp = [e for e in s]
cp = list(s)


"""
print(s)
print(cp)
print(id(s) == id(cp))
"""
cp[0] =100
#print(s)
#print(cp)

"""
    shallow copy

s = [ [10, 20], [30, 40]]
cp = s.copy()
cp = list(s)
cp[0] = 'python'

cp[1][0] = 100

print(s)
print(cp)
"""



"""
 shallow copy

    When we use any of the copy copy methods above, the copy essentially copies all the 
    object references from one sequence to another
    Example: s = [ [10, 20], [30, 40]]

    s = [a, b]        id(s) -> 1000   id(s[0]) -> 2000      id(s[1])  -> 3000
    cp = s.copy()      id(cp) -> 5000     id(cp[0]) -> 2000    id(cp[1])  -> 3000


    When we made a copy of s, the sequence was copied, but it's elements point to the same memory address as the original sequence elements.

    The sequence was copied, but it's elements were not. This is called shallow copy i.e
    it copies the container but not the elements inside.
"""

"""
    deep copy

    So, if collections contain mutable elements, shallow copies are not sufficient to ensure the copy
    can never be used to modify the original 

    Example: deep copy
    s = [ [10, 20], [30, 40]]
    cp = [e.copy() for e in s]

    Exceptions:

    What happens if the mutable elements of s themselves contain mutable elements?

    s = [ [ [0, 1], [2, 3] ], [ [4, 5], [6, 7]]  ], we would need to make at least 3 levels deep to ensure a true deep copy.
    Deep copies, in general, tend to need a recursive approach.


    Deep Copies
    The standard library "copy" module has generic copy and deepcopy operations

    The copy function will create a shallow copy
    The deepcopy function will create a deep copy, handling nested objects, and circular references properly

    Custom classes can implement the __copy__ and __deepcopy__ methods to allow you
    to override how shallow and deep copies are made for you custom objects
"""


"""

s = [ [10, 20], [30, 40]]
cp = [e.copy() for e in s]

print("s: ", s)
print("cp: ", cp)

cp[1][0] = 100

print("s: ", s)
print("cp: ", cp)
"""

class MyClass:
    def __init__(self, a):
        self.a = a 


from copy import copy, deepcopy

x = [10, 20]
obj = MyClass(x)


cp_shallow = copy(obj)

cp_deep = deepcopy(obj)