"""
    p1 = Person('john')
    p2 = Person('john')

    p1 is p2 -> False
    p1 == p2 -> True
    hash(p1)  == hash(p2) -> True

class Person:
    def __init__(self, name):
        self.name = name 

    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return self.name == self.other
        return False

    def __hash__(self) -> int:
        return hash(self.name)

"""

#Custom Classes and Hashing
#NB: A list is not hashable but a tuple 

"""
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t1), id(t2))
print(t1 == t2)
print(t1 is t2)
print(hash(t1), hash(t2))# Two functions equal objects have the  same hash   

d = {t1 : 100}
print(d[t1])
print(d[t2])
print(d)
"""

class Person:
    def __init__(self, id,  name, age):
        self._id = id
        self.name = name
        self.age = age 

    def __repr__(self) -> str:
        return f'Person(id={self._id}, name={self.name}, age={self.age})'

    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return self._id == other._id
        return False

    def __hash__(self) -> int:
        return hash(self._id)



"""
p1 = Person('John', 78)
p2 = Person('Eric', 78)
persons = {p1: 'John Object', p2 :  'Eric object'}

#Since p1 and p2 are hashable, we can use them as keys in the dictionary

for k in persons.keys():
    #print(k)
    pass 
"""


#print(hash(p1))
#print(persons[p2])
#print(persons[Person('John', 78)])


class Number:
    def __init__(self, x) -> None:
        self.x = x

    def __eq__(self, other) -> bool:
        if isinstance(other, Number):
            return self.x == other.x
        return False

    def __hash__(self) -> int:
        return hash(self.x)


class SameHash:
    def __init__(self, x) -> None:
        self.x = x

    def __eq__(self, other) -> bool:
        if isinstance(other, SameHash):
            return self.x == other.x
        return False

    def __hash__(self) -> int:
        return 100


numbers = {Number(x): 'some value' for x in range(1000)}
same_hashes = {SameHash(x): 'some value' for x in range(1000)}

#print(numbers[Number(500)])
#print(same_hashes[SameHash(800)])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, another) -> bool:
        if isinstance(another, tuple) and len(another) == 2:
            another = Point(*another)
        if isinstance(another, Point):
            return self.x == another.x and self.y == another.y 
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))


#pt = Point(1, 2)
#print(pt)

points = {Point(0,0) : 'origin', Point(1,1) : 'second pt'}

print(points[Point(0, 0)])
print(points[(1, 1)])


p1 = Person('john', 'john', 78)
persons = {p1: 'john object'}
print(persons[p1])

p1.name = 'Eric'
p1.age = 75

print(persons[Person('john', None, None)])
