class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)

print("instance: ", isinstance(m, Animal))
print("instance: ", isinstance(m, Mammal))
print("instance: ", isinstance(m, object))

print("subclass", issubclass(Mammal, Animal))
print("subclass", issubclass(Mammal, object))
print("subclass", issubclass(Animal, object))
