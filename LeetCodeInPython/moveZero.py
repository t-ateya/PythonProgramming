"""
    Given an array of integers, write a function to move all 0'S to the end while maintaining the relative order of the elements

    Solutions:
    1. Brute force approach
      -Creat a new array with same size and input
      -Loop over input array and push non-zero elements to the new array
      -Push zeros for the rest of the new array size

    2. Optimal Solution Intuition



"""
from typing import List


def move_zeroes_brute_force(array):
    temp_array = []*(len(array))
    for item in array:
        if item !=0:
            temp_array.append(item)
    new_len = len(array) - len(temp_array)
    for _ in range(new_len):
        temp_array.append(0)   
    return temp_array

def move_zeroes2(array):
    for index in range(len(array)):
        if array[index] == 0:
            array.pop(index)
            array.append(0)
    return array


#Tutor's approach
class Solution:
    def move_zeros(self, nums:List[int]) ->None:
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j +=1
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums 

items = [0, 1, 0,3, 12]
#print(move_zeroes_brute_force(items))
print(move_zeroes2(items))

sol = Solution()
print(sol.move_zeros(items))