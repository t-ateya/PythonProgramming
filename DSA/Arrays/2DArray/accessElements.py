#Day 1- 11, 15, 10, 6
#Day 2- 10, 14, 11, 5
#Day 2- 12, 17, 12, 8
#Day 4- 15, 18, 14, 9

import numpy as np

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

#print(twoDArray)

def accessElements(array, rowIndex, colIndex):
    """Returns the element at given column and row indexes of a 2D array"""
    if rowIndex >= len(array) and colIndex >= len(array([0])):
        print('Incorrect index')
    else:
        return array[rowIndex][colIndex]


#print(accessElements(twoDArray, 1, 17))

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print("\n",array[i][j])
            


traverseTDArray(twoDArray)