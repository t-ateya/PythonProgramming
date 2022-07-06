
def find_biggest_element(arr):
    max_element = arr[0]
    for index in range(1, len(arr)):
        if arr[index]> max_element:
            max_element = arr[index]
    return max_element

arr = [2, 5, 4, 10, 234, 11]
print(find_biggest_element([2, 5, 4, 10, 234, 11]))