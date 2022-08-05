def multiply(*args):
    print(args)
    prod = 1
    for arg in args:
        prod *=arg
    return prod 
    
print(multiply(1,2,3,4,5))
print(multiply(-1))


def add(x, y):
    return x + y

def mul(x, y, z):
    return x*y*z

nums = [3, 5]
print(add(*nums))


nums = {"x":15, "y":25}
nums1 = {"x":15, "y":25, "z":30}
print(add(x=nums["x"], y=nums["y"]))

print(add(**nums))
print(mul(**nums1))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1,2,3,4, operator="*"))