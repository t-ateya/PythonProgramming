from array import array

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.5, 1.3, 1.7])
#print(arr1)
#print(arr2)

arr1.insert(1,3)
arr1.append(9)
#print(arr1)


def traverse_array(arr):
    for index in range(len(arr)):
        print(arr[index])
#traverse_array(arr1)

for i in arr1:
    print(i)