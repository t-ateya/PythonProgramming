myList = [10, 20, 30, 40, 50, 80, 90]

def search_in_List(List, value):
    if value in List:
        return (List.index(value))
    else:
        return (f"The value {value} does not exist in the List")

print(search_in_List(myList, 90))