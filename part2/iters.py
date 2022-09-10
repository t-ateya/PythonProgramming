
import random

"""

class RandomNumbers:
    def __init__(self, length, *, range_min = 0, range_max = 10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.number_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.number_requested >= self.length:
            raise StopIteration
        else:
            self.number_requested +=1
            return random.randint(self.range_min, self.range_max)


numbers = RandomNumbers(5)

while True:
    try:
        #print(next(numbers))
        pass 
    except StopIteration:
        break 
"""


"""
    The iterator Protocol 
    A protocol is simply a fancy way of saying that our class is going to implement a certain functionality that python can count on.

    The iterator protocol is quite simple - the class needs to implement two methods:
      __iter__ This method should just return the object (class instance) itself

      __next__ this method is responsible for handling back the next element from the collection and raising StopIteration except when all elements have been 
                    handed out

    Iterators
        An iterator is therefore an object that implements:
            --iter__ ->just returns the object itself
            --next__ -> returns the next item from the container , or raises StopIteration
        
        If an object is an iterator, we can use it with for loops, comprehension, etc.
"""


class Square():
    def __init__(self, lenght):
        self.i = 0
        self.length = lenght

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __iter__(self):
        return self



sq = Square(5)

"""
while True:
    try:
        item = next(sq)
        #print(item)
        pass
    except StopAsyncIteration:  #Catch the StopIteration

        break
"""


for item in sq:
    print(item)

#N.B: sq is an iterator and cannot be restarted

sq = Square(5)

l = [(item, item + 1) for item in sq]
print(l)

l = list(enumerate(sq))
print(l)