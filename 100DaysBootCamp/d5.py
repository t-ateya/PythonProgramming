fruits = ["Apple", "Peach", "Pear"]

"""
# Day 5.1 Average Height exer
# You are going to write a program that calcs the average student height from a list of heights
# NB.The split method converts input string to list
student_heights = input(
    "Enter a list of student heights separated by space:\n").split(" ")
# print(student_heights)
tot_students = 0
for h in range(0, len(student_heights)):
    student_heights[h] = int(student_heights[h])
    tot_students += 1
# print(student_heights)
# print(tot_students)

sum_of_students = sum(student_heights)
average_height = sum_of_students/len(student_heights)
#average_height = tot_students/len(student_heights)
#print(f"Student  average height is: {average_height}")
"""
"""
# Ex5.2 Print heighest score
student_scores = input("Enter student scores separated by space: \n").split()
# Convert score from  string to int
for score_pos in range(0, len(student_scores)):
    student_scores[score_pos] = int(student_scores[score_pos])

# Find max score
max_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score is: {max_score}")

"""

"""
# Exer 5.3 Adding Evens
# Cal the sum of all the even nums from 1-100
sum = 0
start, stop, step = 0, 5, 2
for num in range(start, stop, step):
    sum += num
# print(sum)

# Alternatively
total = 0
for number in range(0, 5):
    if (number % 2 == 0):
        total += number
print(total)
"""

# Exercise 5.4
"""
    You're going to write a program that automatically prints the solution to the FizzBUzz game

    Your program should print each number from 1 to 100 in turn.
    When the number is divisible by 3 then instead of printing the number it should print "Fizz"

    When the number is divisible by 5 then  instead of printing the number  it should print "Buzz"
    
    And if the  number is divisible by both 3 and 5 e.g. 15 then print instead of print the number  it should print "FizzBUZZ"


"""

for number in range(1, 101):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)
