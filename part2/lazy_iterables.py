
"""
    Lazy Evaluation
        This is often used in class properties
            properties of classes may not always be populated when the object is created
            value of a property only becomes known when the property is requested -deferred

    Example:
    class Actor:
        def __init__(self, actor_id):
            self.actor_id = actor_id
            self.bio = lookup_actor_in_db(actor_id)
            self.movies = None 

        @property
        def movies(self):
            if self.movies is None:
                self.movies = lookup_movies_in_db(self.actor_id)
            return self.movies

    Application to iterables
        We can apply the same concept to certain iterables
        We do not calculate the next item in an iterable until it is actually requested

    Other Examples of lazy eva:
        1. iterable->Factorial(n)
            will return factorials of consecutive integers from 0 to n-1
            do not pre-compute all the factorials
            wait until next requests one, then calculate it

        2. Another application of this might be retrieving a list of forum posts
            Posts might be an iterable
             each call to next returns a list of 5 posts (or some page size)
                but uses lazy loading
                ->every time next is called, go back to database and get next 5 posts

"""

from ast import iter_child_nodes
import math


class Circle:
    def __init__(self, r):
        self._radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None 
    
    @property
    def area(self):
        if not self._area:
            print("Calculating area ...")
            self._area = math.pi * (self.radius ** 2)
        return self._area

"""
c = Circle(1)
print(c.area)
print("===============")
c.radius = 2
print(c.area)
print(c.area)
"""

class Factorials:
    """Factorial iterable"""
    def __init__(self, length):
        self._length = length

    def __iter__(self):
        return self.FactorialIterator(self._length)

    
    class FactorialIterator:
        """The is the iterator class"""
        def __init__(self, length):
            self.length = length
            self._index  = 0

        def __iter__(self):
            return self 

        def __next__(self):
            if self._index >= self.length:
                raise StopIteration
            else:
                result = math.factorial(self._index)
                self._index += 1
                return result

class FactorialsInfinite:
    """Factorial iterable: Returns the iterator"""
    
    def __iter__(self):
        return self.FactorialIteratorInfinite()

    class FactorialIteratorInfinite:
        """The is the iterator class"""
        def __init__(self):
            self._index  = 0

        def __iter__(self):
            return self 

        def __next__(self):
            result = math.factorial(self._index)
            self._index += 1
            return result
            
            

facts = Factorials(5)
#print(list(facts))

fac = FactorialsInfinite()
fact_iter = iter(fac)

for _ in range(7):
    print(next(fact_iter))

    