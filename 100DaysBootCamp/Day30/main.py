
"""
try:
    file = open("file_name.txt")
    fruits_cost = {"Apple":20, "Bananas": 40, "Orange": 60}
    print(fruits_cost["Apple"])
except FileNotFoundError:
    file = open("file_name.txt", "w")
    file.write("Hello buddies")
except KeyError as error_mesage:
    print(f"That key {error_mesage} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    raise TypeError("This is an error that I made up.")
"""
height = float(input("Height: "))
weight = int(input("Weight: "))
bmi = weight/height**2

if height > 3:
    raise  ValueError("Human height should not be over 3 meters. ")