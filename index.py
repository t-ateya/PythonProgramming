s = "weather"

print("The length of the string is: ", len(s))
print("The last digit is: ", s[-1])
print ("Slicing the elements from index 3 to the end: ", s[3:-1] )
print ("Slicing the elements from index 3 to the end: ", s[3:] )
print("Index method: ", s.index('t'))
print("count the number of 'e' elements: ", s.count('e'))

l1= [ 1,1,1,1,1,1,1, 2, 2,4,8, 2, 2,3, 3, 5,5, 26, 27 ]

print("Counting # of elements in a list: ",l1.count(1))

print("Sorting: ", l1.sort())
print("Sort and Reverse: ", l1.sort(Reverse = True))
