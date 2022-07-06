myList = ["a", "b", "c", "d", "e", "f"]
#Slicing
myList[0:2] = ['x', 'y']
print(myList[:])
print(myList)


#Use delete(), pop() and remove() methods to delete and element from a list
myList.pop()
myList.pop(2)
#del myList[1]
#del myList[0:2]

#myList.remove('e')

print(myList)
