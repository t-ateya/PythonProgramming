
#Q3. How to check if an array contains a number in python

import numpy as np

def find_element(array, element):
    """Checks if an element exists in an array and returns its pos"""
    for index in range(len(array)):
        if element == array[index]:
            return index
    else:
        return "Element not found"

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8 ,9, 10])
#print(myArray[6])
print(find_element(myArray,12))