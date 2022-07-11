
"""
    Given an array A of integers, return true if the following conditions are fullfilled
    1. Lenth of the array is bigger or equal to 3
    2. There exists some index i such that:
    a[0] < a[1]...
    a[i] > a[i + 1]> ... a[a.size -1]

    In a nutshell: Find if there is an increasing subarray followed by a decreasing subarray
"""

def is_valid_mountain(array):
    """Returns True if the array elements increase and then decrease. My Solution"""
    n = len(array)
    if n < 3:
        return False
    
    index  = 0 
    while array[index] < array[index + 1]:
        if index + 1== n-1:
            break
        index += 1
    
    #Case where the the array only increases
    if index + 1  == n-1:
        if array[index] < array[index+1]:
            return False
        return True 
    #Case where the array increases anad then decreases
    
    top = index + 1
    while array[top] > array[top + 1]:
        temp = top
        if temp == n-1:
            return True 

        top += 1
        if top== n-1:
            break

    if top == n-1:
        return True 
    else:
        return False

        

#Tutor's solution
from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) ->bool:
        if (len(A) < 3):
            return False

        index = 1
        while (index < len(A) and A[index] > A[index -1]):
            index +=1;
        
        if (index == len(A)):
            return False
        
        while (index < len(A) and A[index] < A[index -1] ):
            index +=1;
        
        return index == len(A)
        

s = Solution()
arr = [1, 2, 3,4,5,9,8,3,4]
print(s.validMountainArray(arr))
print(is_valid_mountain(arr))