try:
    file = open("app.py")
    age = int(input("Enter age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
   # print("Error: ", ex)
    # print(type(ex))
else:
    print("No exceptions were thrown.")
finally:
    # the finally clause is always executed whether we have an exception or not
    # This is the best place to close files, network connections, db connections, etc
    file.close()
