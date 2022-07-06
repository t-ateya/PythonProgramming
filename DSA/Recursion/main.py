def recursiveMethod(n):
    if n < 1:
        return
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)


# recursiveMethod(5)

def factorial(n):
    if n < 0 or int(n) != n:
        print(f"{n} must be a positive integer!")
        return
    if n in [0, 1]:
        return 1
    else:
        return n*factorial(n-1)


# print(factorial(9.5))
def fibonacci(n):
    if n < 0 or int(n) != n:
        print(f"{n} must be positive integer")
        return
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(11))
