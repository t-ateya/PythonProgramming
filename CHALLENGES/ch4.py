"""
    Write a function that finds out if sum of two elements in an unsorted array is equal to a given target
"""

def two_sum(array, target):
    """prints elements whose sum equals a given target"""
    array.sort()
    left = 0 
    right = len(array) - 1

    while left < right:
        sum = array[left] + array[right]
        if  sum == target:
            print(f"{array[left]} + {array[right]} = {target}")
            
        if sum < target:
            left += 1
        else:
            right -= 1

arr = [4,5,3,2,1,7,6]

two_sum(arr, 7)

        