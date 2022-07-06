import math

"""  
    -Quick sort is a divide and conquer algorithm
    -Find pivot number and make sure smaller numbers located at the left of pivot
    and bigger numbers are located at the right of the pivot
    -Unlike merge sort extra space is not required

    When to use quick sort:
        - When average expected time is O(NlogN)

    When to avoid Quick Sort?
        - When space is a concern
        - When you need stable sort


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


def merge(custom_list, l, m, r):
    n1 = m-l + 1
    n2 = r - m

    L =[0]*n1
    R = [0]*n2

    for i in range(0, n1):
        L[i] = custom_list[l + i]
    
    for j in range(0, n2):
        R[j] = custom_list[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            custom_list[k] = L[i]
            i += 1
        else:
            custom_list[k] = R[j]
            j +=1
        k += 1
    
    while i < n1:
        custom_list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        custom_list[k] = R[j]
        j += 1
        k += 1
    
def merge_sort(custom_list, l, r):
    """ l is the right index of the custom list that needs to be sorted while r is the right index"""
    if l<r:
        m = (l + (r-1))//2
        merge_sort(custom_list, l, m)
        merge_sort(custom_list, m+1, r)
        merge(custom_list, l, m, r)
    return custom_list

def partition(customList, low, high):
    i = low -1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i +=1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i + 1], customList[high] = customList[high], customList[i+1]
    return (i + 1)

def quick_sort(custom_list, low, high):
    if low < high:
        pi = partition(custom_list, low, high)
        quick_sort(custom_list, low, pi-1)
        quick_sort(custom_list, pi+1, high)



#customList = [5, 9,1,2,8,4,7,6]
customList = [2,1,7,6,5,3,4,9,8]

quick_sort(customList, 0, len(customList)-1)
print(customList)




