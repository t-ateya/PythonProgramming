
"""
    def key(p):
        reuturn p.age

    key = lambda p : p.age

    def key(s):
        return s[-1]

    key = lambda s: s[-1]

    Python sorted function
            sorted[iterable, key=None, reverse = False]

    The sorted function:
        -sorted does not modify the iterable(sequence)
        -it simply makes a copy of the iterable
        -returns the sorted elements in a list
        -uses a sort algorithm called TimSort
        - a stable sort


    Stable Sorts
        A stable sort is one that maintains the relative order of items that have equal keys

        p1.age -> 30
        p2.age -> 15
        p3.age -> 5
        p4.age -> 32
        p5.age -> 15

        sorted((p1, p2, p3, p4, p5), key=lambda p : p.age) ==>p3,p2,p5,p1,p4


    In-Place Sorting (no copy is made prior to sorting)
     If the iterable is mutable, in place sorting is possible
     But that will depend on the particular type you're dealing with.
     Python's list objects support in-place sorting 

     The list class has a sort() instance method that does in-place sorting

     Note:
     sorted() makes a copy of the list before sorting and does not mutable the iterable if t's mutable
     sort() does not make a copy of the list. It sorts it directly and might mutate the iterable if's mutable 

     l = [10, 5, 3, 2]

     l.sort()

     l->[2,3,5,10]

"""



t = 10, 3, 5, 8, 9, 6, 1
#print(sorted(t))
#print(t)


s = {10, 3, 5, 8, 9, 6, 1}
#print(sorted(s))
#print(s)

d = {3:100, 2:200, 1:30}
#print(list(d))
#print(sorted(d))

d = {'a':100, 'b':50, "c":10}

#print(sorted(d, key=lambda k : d[k]))

t = 'this', 'parrot', 'is', 'a', 'late', "bird", 
#print(t)
#print(sorted(t, key= lambda x: len(x)))
#print(sorted(t, key= lambda x: -len(x)))  #-len(x) === len(x), reverse = True

def sort_key(s):
    return len(s)

#print(sorted(t, key=sort_key))

t = "aaaa", 'bbbb', 'e'*4, 'dddd', 'c'*4

#print(sorted(t, key = lambda s: len(s)))

t = 0, 10 + 10j, 3-3j, 4+4j, 5-2j

#print(sorted(t, key=abs))

#print(sorted(t, key=lambda c:c.imag))

#print(sorted(t, key=lambda c:c.imag, reverse=True))

l = "this bird is a late parrot".split(" ")
#print(l)

result = l.sort(key=lambda s: len(s))
#print(result)

#print(l)

class MyClass:
    def __init__(self, name, val) -> None:
        self.name = name 
        self.val = val 

    def __repr__(self) -> str:
        return f'MyClass({self.name}, {self.val})'

    def __lt__(self, other):
        print("Calling __lt__")
        if isinstance(other, MyClass):
            return self.val < other.val 
        raise TypeError("other must be of type MyClass")

c1 = MyClass('c1', 20)
c2 = MyClass('c2', 10)
c3 = MyClass('c3', 20)
c4 = MyClass('c4', 10)

#print(c1 < c4)
#print(sorted([c1, c2, c3, c4]))

l = [c4, c2, c3, c1]

print(sorted(l))

print(sorted(l, key=lambda c : c.name))



