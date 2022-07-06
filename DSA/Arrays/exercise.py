from array import array
#1. Create an array and traverses

my_array = array(['i', [1, 2, 3, 4, 5]])
for i in my_array:
    print(i)
#2. Access individual elements through indexes
print("Step 2")
print(my_array[3])

#3. Append any value to the array suing insert() method

print("Step 3")
print(my_array.append(6))
print(my_array)

#4. Insert value in an array using insert() method
print("Step 4")
my_array.insert(3, 11)
print(my_array)

#5. Extend python array using extend() method
print("Step 5")
my_array1 = array('i', [10, 11, 12])
my_array.extend(my_array1)
print(my_array)


#6. Remove any array from element using remove() method
print("Step 6")
my_array.remove(11)
print(my_array)

#7. Add items from list into array using fromlist() method

#8. Remove last array element using pop() method

print("Step 8")
my_array.pop()
print(my_array)

#9. Fetch any element using its index through index() method
print("Step 9")
print(my_array.index(2))
#10 Reverse a python array using reverse() method

print("Step 10")
print(my_array.reverse())
#11. Get array buffer info through buffer_info() method
#12. Convert array to string using tostring() method
print("Step 12")
strTemp = my_array.tostring()
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(strTemp)
 
#13. Check for number of occurrences of an element using count() method
print("Step 13")
my_array.append(11)
print(my_array.count(11))
print(my_array)
#14. Convert an array to a python list with same elements using tolist() method
#15. Append a string to char array using fromstring() method
#16. Slice Elements from an array
print(my_array[:])
