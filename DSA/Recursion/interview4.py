from unittest import result


def decimal_to_binary(num):
    """Converts a given decimal number to binary"""
    assert int(num) == num, "The parameter must be an integer only!"
    if num==0:
        return 0
    else:
        return (num%2) + 10*decimal_to_binary(int(num/2))
    
#print(decimal_to_binary(13))

arr = [1, 2, 3,4, 5]
for x in arr:
    for y in arr:
        print(x,y)