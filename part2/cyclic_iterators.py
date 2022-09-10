
"""
    1 2 3 4 5 6 7 8 9 
    N S W E
    1N 2S 3W 4E 5N 6S 7W 8E 9N 10S
"""

from typing import Iterable


class CyclicIteratorFinite:
    def __init__(self, lst, length):
        self._lst = lst 
        self._index = 0
        self._length = length

    @property 
    def lst(self):
        return self._lst

    def __iter__(self):
        return self 

    def __next__(self):
        if self._index >= self._length:
            raise StopIteration
        else:
            result = self.lst[self._index % len(self.lst)]
            self._index +=1
            return result

class CyclicIterator:
    """This is a sequence class because we used index"""
    def __init__(self, lst):
        self._lst = lst 
        self._index = 0
    
    @property 
    def lst(self):
        return self._lst

    def __iter__(self):
        return self 

    def __next__(self):
        result = self.lst[self._index % len(self.lst)]
        self._index +=1
        return result


class CyclicIteratorForAllIterables:
    def __init__(self, iterable):
        self._iterable = iterable 
        self.iterator = iter(self._iterable) #create an iterator once and use it when __next__ is called
        """The is an iterable and not a sequence. Therefore, we do not need and index"""
    
    def __iter__(self):
        return self 

    def __next__(self):
        try:
            item = next(self.iterator)
            return item 
        except StopIteration:
            item = self.iterator = iter(self._iterable) #Recreate the iterator
        finally:
            return item
        

        


#iter_cycl = CyclicIteratorFinite("NSWE", 15)
iter_cycl = CyclicIterator("NSWE")
#iter_cycl = CyclicIterator([10,20,35])

"""
for _ in range(5):
    print(next(iter_cycl))
"""

    

numbers = list(range(1,11))


#print(next(iter_cycl))

#print(numbers)

zip_list = list(zip(numbers, iter_cycl))
print(zip_list)

#Not using zip function

print("===============Not using zip function ==================")

n = 10

"""
for i in range(1, n+1):
    direction = next(iter_cycl)
    print(f"{i}{direction}")
"""

#lc = [f"{i}{next(iter_cycl)}" for i in range(1, n+1)]

lc = [str(i) + next(iter_cycl) for i in range(1, n+1)]
print(lc)

items = [str(number) + direction
        for number, direction in zip(range(1, n + 1), iter_cycl)]

print(items)

new_l = [str(number)+ direction for number, direction in zip(range(1, 11), 'NSWE'*(n//4 + 1))]
print(new_l)

print("========Using python built-in module============")
import itertools

n = 10
iter_cycl = itertools.cycle("NSWE")
items = ["{0}{1}".format(i, next(iter_cycl)) for i in range(1, n+1)]
#print(items)

#print(help(itertools.cycle))



