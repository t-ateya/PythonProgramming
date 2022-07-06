# Random password gen

import random
from secrets import choice
import string  # to get asci letters


def gen_random_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "[@_!$%^&*()<>?/\|}{~:]#"

    number_of_letters = int(input(
        "How many letters would you like in your password?\n"))
    number_of_symbols = int(input("How many many symbols would you like?\n"))
    number_of_numbers = int(input("How many numbers would you like?\n"))

    random_letters = ''.join([random.choice(letters)
                             for n in range(number_of_letters)])
    random_symbols = ''.join([random.choice(symbols)
                             for n in range(number_of_symbols)])
    random_numbs = ''.join([random.choice(numbers)
                            for n in range(number_of_numbers)])
    password = [random_letters+random_symbols+random_numbs]

    rand_pass = random.choice(password)
    return rand_pass


# print(letters)
#random_choice = random.choices(letters, k=4)
# print(string.digits)
#passwd = gen_random_password()
#print(f"Your random password is: {passwd} ")

# Another approach for day5 proj
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would like?\n"))

# Eazy Level:  fgh^&23

"""
password = ""
for char in range(1, nr_letters+1):
    password += random.choice(letters)
for char in range(1, nr_symbols+1):
    password += random.choice(symbols)
for char in range(1, nr_numbers+1):
    password += random.choice(numbers)
print("EZ Level: ", password)
"""
# Hard Level:  g^2jk8&

password_list = []
for char in range(1, nr_letters+1):
    password_list += random.choice(letters)
for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)


#passwd = random.shuffle(new_password)
print("p_list", password_list)
random.shuffle(password_list)
password = ""

for char in password_list:
    password += char
print(f"Hard Level: {password}")

# nr_letters  =
