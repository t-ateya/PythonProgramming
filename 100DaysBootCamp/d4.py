import random
from turtle import position


"""
random_integer = random.randint(1, 10)
# print(random_integer)

random_float = random.random()*100
print(random_float)

love_score = random.randint(1, 100)
#print(f"Your love score is {love_score}")


# Exercise=========================
random_side = random.randint(0, 1)
if random_side == 1:
    pass
    # print("Heads")
else:
    pass
    # print("Tail")

name_lists = ["Terence", "Kelly", "Emeka"]
name_chosen = random.choice(name_lists)
#print(f"Name chosen: {name_chosen}")

"""

########### List ##############################
states_of_america = ["Maryland", "Arizona", "Illinois", "California"]
# print(states_of_america[2])
states_of_america.extend(["New York", "NC", "Colorado"])
#print("States of america:", states_of_america)


# Exercise2: Banker Roulette exercise
# 1. Split string method
"""
name_string = input("Give me everybody's names separated by comma.\n")
names = name_string.split(",")
print("Name at pos 0", names[0])
random_name = random.choice(names)
print(random_name,
      f"is going to buy the meal today! in a team of {len(names)}")
"""


# . Nested list
fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[1][1])

# Day 4.3 Treasure  Map
row1 = ["😂", "🤷‍♀️", "😜"]
row2 = ["🙌", "👌", "🤞"]
row3 = ["😜", "😜", "😜"]
chess_board = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])

chess_board[horizontal-1][vertical-1] = "X"
# print(chess_board)
print(f"{row1}\n{row2}\n{row3}")
