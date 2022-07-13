"""
    Given an array of integers sorted in ascending order, find the starting and ending pos of given target value
    - I.e Find the index of the first occurrence and index of the last occurrence of given target value in an array
"""

#My Solution
from typing import final


def find_first_last_pos(array:list[int], target: int)->list[int, int]:
    m = {}
    left = 0
    right = len(array)-1

    if len(array) ==0:
        return "Empty array"

    if len(array) == 1:
        return [left,right] if array[0] == target else [-1,-1]
    
    while array[left] != target and left != len(array)-1:
        left +=1
    
    if left == len(array)-1:
        return [left,left]
    m[array[left]] = left

    for x in range (left + 1, right+1):
        if array[x] == target:
            m[array[left]] += 1
    return [left, m[array[left]]]

    


#Tutor's solution
class Solution:
    #Use Binary Search Approach since the array is sorted
    def getLeftPosition(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right)//2
            if (nums[mid] == target):
                if (mid-1>=0 and nums[mid-1] != target or mid ==0 ):
                    return mid
                right = mid - 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def getRightPosition(self, nums, target):
        left = 0
        right = len(nums) -1
        while (left <= right):
            mid = (left + right)//2
            if (nums[mid] == target):
                if (mid+1 < len(nums) and nums[mid+1] != target or mid == len(nums) -1 ):
                    return mid
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1


    def searchRange(self, nums:list[int], target: int) ->list[int]:
        left = self.getLeftPosition(nums,target)
        right = self.getRightPosition(nums,target)
        return [left, right]


sol = Solution()
array = [10,12,13,14,15,15,19]
print(find_first_last_pos(array, 17))
print(sol.searchRange(array, 17))


