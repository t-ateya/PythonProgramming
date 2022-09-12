
"""
    Making an iterator to iterate over any sequence


class SeqIterator:
    def __init__(self, seq):
        self.seq = seq 
        self.index = 0

    def __iter__(self):
        return self 

    def __next__(self):
        try:
            item = self.seq[self.index]
            self.index += 1
            return item 
        except IndexError:
            raise StopIteration()

Calling iter()
    -When the iter(obj) is called, python first looks for an __iter__ method.
    If it's there, it used it.
    If it's not there, it looks for a __getitem__method . If it's there, create an iterator object and return that
    if it's not there, raise a TypeError exception (not iterable)

Checking if an object is iterable
"""



"""

class SeqIterator:
    def __init__(self, seq):
        self.seq = seq 
        self.index = 0

    def __iter__(self):
        return self 

    def __next__(self):
        try:
            item = self.seq[self.index]
            self.index +=1
            return item 
        except IndexError:
            raise StopIteration()

So when iter(obj) is called:
    python first looks for an __iter__ method:
     -> if it's there, it uses it
     -> if it's not:
        -> if looks for __getitem__ method
            -> if it's there create an iterator object and return it.
            -> if it's not there, raise a TypeError exception(not iterable)

    Testing if an object is iterable

    1. Check if they implement __getitem__ or __iter__ and that __iter__ returns and iterator

    2. Easier approach
            try:
                iter(obj)
            except TypeError
               #not iterable 
               <code>
            else:
                # is iterable
                <code>
"""

class Squares:
    def __init__(self, n):
        self._n = n 

    def __len__(self):
        return self._n 

    def __getitem__(self, i):
        if i >= self._n:
            raise IndexError
        else:
            return i**2

class SquaresIterator:
    def __init__(self, squares):
        self._squares = squares
        self._i = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self._i >= len(self._squares):
            raise StopIteration
        else:
            result = self._squares[self._i]
            self._i += 1
            return result



class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._i = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self._i >= len(self._sequence):
            raise StopIteration
        else:
            result = self._sequence[self._i]
            self._i += 1
            return result

class SimpleIter:
    def __init__(self):
        pass

    def __iter__(self):
        return 'Nope'



s = SimpleIter()
sq = Squares(5)

"""
sq_iter = iter(sq)


for i in sq:
    print(i)

print(type(sq_iter))

print('__next__' in dir(sq_iter))

print(next(sq_iter))
print(next(sq_iter))
"""

sq_iterator = SquaresIterator(sq)

print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))

#print('__iter__' in dir(s)) #This approach is not reliable as the __iter__() does not return self

#print(iter(s))  #best way to check if an obj is iterable

def is_iterable(obj):
    try:
        iter(obj)
        return True 
    except TypeError:
        return False

#print(is_iterable(s))
#print(is_iterable(Squares(5)))

obj = 100
if is_iterable(obj):
    for i in obj:
        print(i)
else:
    print("Error: obj is not iterable")

try:
    for i in obj:
        print(i)
except TypeError:
    print("Error: obj is not iterable")