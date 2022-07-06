try:
    with open("app.py") as file, open("tuple.py") as target:
        print("File opened.")
        file.__ex
    age = int(input("Enter age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
   # print("Error: ", ex)
    # print(type(ex))
else:
    print("No exceptions were thrown.")
