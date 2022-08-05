def divide(dividend, divisor):
    """Returns the result of dividing a number by a non-zero number"""
    if (divisor == 0):
        raise ZeroDivisionError("Divisor cannot be zero. Please change the divisor")
    return dividend / divisor

grades = [60, 90]

print("Welcome to the average grade program")
try:
    average_grade = divide(sum(grades), len(grades))
except ZeroDivisionError as error:
    print(error)
    print("There are no grades yet in your list.")
except ValueError:
    pass 
else:
    print(f"The average grade is {average_grade}")
finally:
    print("Thank you")
    

print("================================================")
students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"];
        grades= student['grades']
        average = divide(sum(grades), len(grades))
        print(f"{name} has average {average}")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades")
else:
    print("--All student grades calculated--")
finally:
    print("--End of student average calculation--")
