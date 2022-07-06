"""
    - Bubble sort is also referred to as Sinking Sort
    - We repeatedly compare each pair of adjacent items and swap them if there're in wrong order

"""

def bubbleSort(customList):
    """This function sorts a list in ascending order"""
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j+1] = customList[j + 1], customList[j]
                
    return customList
def bubbleSort2(customList):
    """This function sorts a list in ascending order.My approach"""
    for i in range(len(customList)-1):
        for j in range(i+1,len(customList)):
            if customList[i] > customList[j]:
                customList[i], customList[j] = customList[j], customList[i] 
    return customList


"""
    When to use Bubble Sort:
        - When the input is already sorted
        - Space is a concern
        - Easy to implement

    When to avoid Bubble Sort?
        - Average time complexity is too poor
"""


customList = [5, 9,1,2,8,4,7,6]
print(customList)
bubbleSort2(customList)
print(customList)