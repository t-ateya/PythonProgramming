"""
    
    -Divide the given array into two parts
    -Take first element from unsorted array and find its correct position in sorted array
    -Repeat until sorted array is empty

        When to use insertion sort:
            -When we have insufficient memory
            -Easy to implement
            -When we have continous inflow of numbers and we want to keep them sorted

        When to avoid Insertion Sort:
            - When time is concern
"""

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)



def insertion_sort(custom_List):
    """Sort a list in ascending order"""
    for i in range(1, len(custom_List)):
        key = custom_List[i]
        j = i-1
        while j>=0 and key < custom_List[j]:
            custom_List[j+1] = custom_List[j]
            j -= 1
        custom_List[j+1] = key
    print(custom_List)



#customList = [5, 9,1,2,8,4,7,6]
customList = [2,1,7,6,5,3,4,9,8]
insertion_sort(customList)




