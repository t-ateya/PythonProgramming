
newTuple = ('a', 'b','c','d','e')

def searchTuple(pTuple, element):
    if element in pTuple:
         return pTuple.index(element) 
    else:
        return f"The element {element} does not exist"


print(searchTuple(newTuple, "f"))