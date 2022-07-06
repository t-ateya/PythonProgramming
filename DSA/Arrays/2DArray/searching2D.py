#Day 1- 11, 15, 10, 6
#Day 2- 10, 14, 11, 5
#Day 2- 12, 17, 12, 8
#Day 4- 15, 18, 14, 9

import numpy as np

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

#print(twoDArray)

def searchTDArray(array, value):
    """Returns the position of an element in a given 2D array"""
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is found at index: '+ str(i)+"" +str(j)
    return (f"The value {value} is not found in the array")

print(searchTDArray(twoDArray,18))
#BigO(mn), where m is number of rows and n number of cols