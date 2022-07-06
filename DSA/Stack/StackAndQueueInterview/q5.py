"""
    Q5. Animal Shelter
    An animal shelter, which holds only dogs and cats, operates strictly "first in, first out" basis. People must adopt either the "oldest"
    (based on arrival time) of all the animals at the shelter, or they can select whether they would prefer a dog or a cat( and will receive the oldest
    animal of that type). They can select which animal they would. Create the data structures to maintain this system and implement operations such as enqueue
    , dequeueAny, dequeueDog, and dequeueCat. 
"""


class AnimalShelter():
    def __init__(self):
        self.dogs = []
        self.cats = []


    def enqueue(self, animal, type):
        if type.title() == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
            
        else:
            return self.cats.pop(0)


    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
            
        else:
            return self.cats.pop(0)
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
            
        else:
            return self.dogs.pop(0)

    def dequeueAny(self):
        if len(self.cats) == 0 and len(self.dogs) !=0:
            result = self.dogs.pop(0)
        else:
             result = self.cats.pop(0)
        return result

customQ = AnimalShelter()
#print(customQ.dequeueAny())
customQ.enqueue("Cat1", "Cat")
customQ.enqueue("Cat2", "cat")
customQ.enqueue("Dog1", "Dog")
customQ.enqueue("Cat3", "Cat")
customQ.enqueue("Dog2", "Dog")


print(customQ.dequeueDog())
print(customQ.dequeueCat())
print(customQ.dequeueAny())