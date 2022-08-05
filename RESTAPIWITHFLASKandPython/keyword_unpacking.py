
def name(**kwargs):
    print(kwargs)

#name(name = "Bob", age=25)

def named(name, age):
    print(name, age)


details = {"name": "Ateya", "age":28}
data = ["arrey", 28]
named(**details)
name(**details)
#print(*data)

def print_nicely(**kwargs):
    name(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}:{value}")


print_nicely(name="Bob", age=25)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="ateya", age=26, hobby="programming")
