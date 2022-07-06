from array import array 

arr1 = array('i', [1,2,3,4,5,6])

def searchInArray(arr, value):
    if value not in arr:
        print(f"{value} not in the array")
    else:
        for element in arr:
            if element == value:
                pos = arr.index(value)
                print(f"{value} is found in the array at position {pos}")

    



#searchInArray(arr1,6)

def searchElement(arr, value):
    for i in arr:
        if i == value:
            return arr.index(value)
    return "The element is not found in array"

print(searchElement(arr1,6))