from array import array

arr2 = array('d', [1.5, 1.3, 1.7])


def access_element(array, index):
    if index > len(array):
        print(f"There is no element at index {index}")
    else:
        print(array[index])



#access_element(arr2, 8)

print(arr2.tostring())
