
#How to find the missing number in an integer array of 1 to 100?

def get_missing_num(myList):

    sum_n_terms = ((len(myList) + 1)*(len(myList) + 2))/2
    sum_of_list = sum(myList)
    missing_number = sum_n_terms - sum_of_list
    print(f"The missing number is: {int(missing_number)}")


myList = [1, 2, 3, 4, 5,6,7, 8, 10]

get_missing_num(myList)