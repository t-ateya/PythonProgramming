
import math 
def binary_search(array, value):
    """Searches a value in a given array"""
    start = 0
    end = len(array) -1
    middle = math.floor((start + end)/2)
    while not(array[middle]==value) and start <= end:
        if value < array[middle]:
            end = middle -1
        else:
            start = middle + 1
        middle = math.floor((start + end)/2)
    if array[middle]==value:
        return middle
    else:
        return -1




customArray = [0,9,12,15,17,19,21,28]
print(binary_search(customArray, 29))