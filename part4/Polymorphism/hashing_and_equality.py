#Hashing and Equality

#print(dir(object))

class Person:
    def __init__(self, name) -> None:
        self._name = name 

    @property
    def name(self):
        return self._name

    def  __hash__(self) -> int:
        return hash(self.name)
        
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    def __repr__(self) -> str:
        return f'Person(name={self.name})'

p1 = Person('John')
p2 = Person('John')
p3 = Person('Mary')

print(hash(p1), hash(p2))

print(p1==p2)