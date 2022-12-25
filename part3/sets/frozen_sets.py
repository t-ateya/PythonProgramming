"""
    Frozen Sets
       -Immutable sets. Same properties as sets
       - Their elements can be mutable
       - If all elements in a frozen set are hashable, then the frozen set is also hashable
       -> can be used as key in a dictionary
       -> can be an element of another set

    l1 = [1, 2, 3]       l2 = list(l1)             l1 is l2 -> False
    t1 = (1, 2, 3)        t2 = tuple(t1)           t1 is t2 ->True

    s1 = frozenset({1, 2, 3})
    s2 = frozenset(s1) or s2 = s1.copy()
    s1 is s2 => True
"""
s1 = frozenset("ab")
s2 = {1, 2}
s3 = s1 | s2
#print(s3)

class Person:
    def __init__(self, name, age):
        self._name = name 
        self._age = age 

    def __repr__(self):
        return f"Person(name={self._name}, age={self._age})"

    @property
    def name(self):
        return self._name 

    @property
    def age(self):
        return self._age

    def key(self):
        return frozenset({self.name, self.age})

p1 = Person('John', 78)
p2 = Person('Eric', 75)

d = {p1.key() : p1, p2.key():p2}

#print(d[frozenset(['John', 78])])
#print(d[frozenset([78, 'John'])])

from functools import lru_cache

@lru_cache
def my_func(*, a, b):
    print("calculating a+b ...")
    return a + b

my_func(a=1, b=2)
    

def memoizer(fn):
    cache = {}
    
    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key not in cache:
            result = fn(*args, **kwargs)
            cache[key] = result
        return cache[key]
    return inner


@memoizer
def my_func(*, a, b):
    print("Calculating a + b ...")
    return a + b
            

def memoizer2(fn):
    cache = {}
    def inner(*args, **kwargs):
        key = frozenset(args) | frozenset(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result 
    return inner
        