"""
    Sequence types, at a minimum, implement the following methods:
    __len__
    __getitem__

    The __getitem__ method should return an element of the sequence based on the specified index or 
    raise an IndexError exception if the index is out of bounds.
"""



"""
my_list = ['a', 'b', 'c', 'd', 'e', 'f']

l = [0, 1, 2, 3, 4, 5]
print(my_list.__getitem__(0))
print(my_list.__getitem__(1))
print(my_list.__getitem__(-1))
print(my_list.__getitem__(slice(None, None, -1)))
#print(my_list.__getitem__(-100))
#print(my_list.__getitem__(100))


print("=============================================")
index = 0
while True:
    try:
        item = l.__getitem__(index)
    except IndexError:
        break 
    print(item**2)
    index += 1

print("===============================================")

print(len(l))
print(l.__len__())
"""

class Silly:
    def __init__(self, n):
        self.n = n 
    
    def __len__(self):
        print("Called __len__")
        return 'this is silly'

    def __getitem__(self, value):
        print(type(value))
        print(f"You requested item at {value}")
        return 'This is a silly element'

silly = Silly(10)
silly[0:5:2]
    