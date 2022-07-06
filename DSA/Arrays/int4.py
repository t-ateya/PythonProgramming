
#Q4. How to find max product of two integers in the array where all elements are positive
from random import randrange
import numpy as np

def find_max_product(array):
    """Returns the maximum product of any two integers in an array"""
    max =1
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]*array[j] > max:
                max = array[i]*array[j]
                pairs = str(array[i]) + "," + str(array[j])
    print(f"({pairs})")
    return (max)

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8 ,9, 10,12])

print(find_max_product(myArray))