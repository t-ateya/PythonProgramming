#Day 1- 11, 15, 10, 6
#Day 2- 10, 14, 11, 5
#Day 2- 12, 17, 12, 8
#Day 4- 15, 18, 14, 9

import numpy as np

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

#print(twoDArray)

#axis =1 =>column and axis = 0 =>rows
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)

#print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[4, 3, 2, 1]], axis=0)

print(newTwoDArray)
print(newTwoDArray[0])
print(len(newTwoDArray[0]))
print(len(newTwoDArray))