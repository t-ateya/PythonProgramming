################## DEBUGGGING  #################

# Describe problem
from random import randint


def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


# my_function()


# Reproduce the bug
"""
dice_imgs = ["0", "0", "0", "0", "0", "0"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
"""

# Play Computer
"""

year = int(input("What's your year of birth?: "))
if year > 1980 and year < 1994:
    print("You're millenial")
elif year > 1994:
    print("You're a Gen Z.")
"""

# Print is Your Friend

"""

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages*word_per_page
print(total_words)
"""
# Use a debugger


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item*2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 45, 6])
