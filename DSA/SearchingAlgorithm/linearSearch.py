def linear_search(array, item):
    """Searches and item in a list and returns the index of the item. Otherwise returns -1"""
    for index in range(len(array)):
        if array[index] == item:
            return index
    return -1

cL= [2,3,4,1,9]
print(linear_search(cL, 8))