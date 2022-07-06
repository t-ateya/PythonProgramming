def increment(number, by=1):
    return (number, number + by)


print(increment(5, by=3))

#   python sees an asterick * before a parameter as a tuple


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print("mult: ", multiply(2, 3, 6))
