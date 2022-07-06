#find out the runtime of the code below
def foo(array):
    sum = 0
    product =1
    for i in array:
        sum += i

    for i in array:
        product *=i 
    print("Sum = "+str(sum) + ", Product = "+str(product))

#Ans: BigO(N)