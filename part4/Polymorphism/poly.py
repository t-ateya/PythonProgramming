from numbers import Real


class Vector:
    def __init__(self, *components):
        if len(components) < 1:
            raise ValueError('Cannot create an empty vector.')
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f"Vector components must all be real numbers. {component} is invalid")
        self._components = tuple(components)

    def __len__(self):
        return len(self._components)

    @property 
    def components(self):
        return self._components

    def __repr__(self):
        return f"Vector{self.components}"

    def validate_type_and_dimension(self, v):
        return isinstance(v, Vector) and len(v) == len(self)

    def __add__(self, other):
        if not self.validate_type_and_dimension(other):
            return NotImplemented

        components = (x + y for x, y in zip(self.components, other.components))
        return Vector(*components)



class Person:
    def __init__(self, name):
        self.name = name 

    def __repr__(self) -> str:
        return f'Person({self.name})'

class Family:
    def __init__(self, mother, father) -> None:
        self.mother = mother 
        self.father = father 
        self.children = []

    def __iadd__(self, other):
        self.children.append(other)
        return self
f = Family(Person('Mary'), Person('John'))

# p1 = Person("Peter") 
# print(p1)  
f += Person('Eric') 
f += Person('Michael') 
print(f.mother)
print(f.father)
print(f.children)