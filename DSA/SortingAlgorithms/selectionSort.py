"""
    -In case of selection sort, we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted.
"""

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


customList = [5, 9,1,2,8,4,7,6]
selectionSort(customList)


"""
    When to use Selection Sort?
        - When we have insufficient memory
        - Easy to implement

    When to avoid Selection sort?
        -When time is a concern
"""