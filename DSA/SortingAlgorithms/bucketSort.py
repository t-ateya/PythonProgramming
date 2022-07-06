import math

"""  
    -Create buckets and distribute elements of array into buckets
    -Sort buckets individually
    -Merge buckets after sorting

        When to use bucket sort:
            - When input is uniforly distributed over range

        When to avoid Bucket sort?
            -When space is concern
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
    return custom_List


def bucket_sort(custom_list):
    """Sorts elements in a list using bucket algo"""
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    arr = []
    [arr.append([]) for i in range(len(custom_list)) ]

    for num in custom_list:
        index_b = math.ceil(num*number_of_buckets/max_value)
        arr[index_b-1].append(num)

    for i in range(number_of_buckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            custom_list[k] = arr[i][j]
            k += 1
    return custom_list










#customList = [5, 9,1,2,8,4,7,6]
customList = [2,1,7,6,5,3,4,9,8]
print(bucket_sort(customList))




