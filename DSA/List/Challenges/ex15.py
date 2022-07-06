#Write a function that takes a list and returns a new list that contains all but the first and last elements

def middle(lst):
    lst.pop(0)
    lst.pop()
    return lst
myList = [1, 2, 3, 4]
myList2 = [1, 2, 3, 4]

def Middle(lst):
    new = lst[1:]
    del new[-1]
    return new

print(middle(myList))
print(Middle(myList2))