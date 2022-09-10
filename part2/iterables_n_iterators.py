
"""
    An iterable is something fit for iterating over
    iterator:
        - get next item, no index needed.


    Example: Sets

    sets are unordered collections of items e.g s ={'x', 'y', 'b', 'c', 'a'}

    sets are not indexable

    The concept of next
    For general iteration, all we really need is the "get the next item" in the collection


Example:
class Square():
    def __init__(self):
        self.i = 0

    def next_(self):
        result = self.i ** 2
        self.i += 1
        return result

"""


"""
class Square():
    def __init__(self, lenght):
        self.i = 0
        self.length = lenght

    def __next__(self):
        if self.i >= self.length:
            raise StopAsyncIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Square(5)

while True:
    try:
        item = next(sq)
        print(item)
    except StopAsyncIteration:  #Catch the StopIteration
        break
"""



"""
    The collection is iterable
            but the iterator is responsible for iterating over the collection

    The iterable is created once(collection of data) while the 
    The iterator is created every time we need to start a fresh iteration.


    Iterable vs Iterator

    An iterable is an object that implements
    __iter__ and returns an iterator (in general, a new instance)

    An iterator is an object that implements 
        __iter__ and returns itself (an iterator) (not a new instance)

        __next__ returns the next method

    Iterators are themselves iterables buth they are iterables that become exhausted

    Iterables on the other hand never become exhausted b/c they always
    return a new iterator that is then used to iterate.

    Iterating over an iterate
        Python has  a built-in function iter(). It calls the __iter__ method.

    The first thing Python does when we try to iterate over an object is, it calls iter() to obtain an iterator
        then it starts iterating (using next, StopIteration, etc) using the iterator returned by iter()
"""