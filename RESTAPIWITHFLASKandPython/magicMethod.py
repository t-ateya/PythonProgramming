class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    """
    def __str__(self) -> str:
        return f"Person {self.name}, {self.age} years old."
    """

    def __repr__(self) -> str:
        return f"<Person({self.name}, {self.age})>"


p= Person("Paul", 25)
print(p)