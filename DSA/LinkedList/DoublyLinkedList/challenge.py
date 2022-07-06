"""
n = 10
i = 0
while i < n:
    i +=1
    if i%2 ==0:
        continue
    print(i)
"""

def get_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    return name, age, gender


def play_game():
    should_continue = True 
    while should_continue:
        name, age, gender = get_info()
        print(f"Your name is:  {name}, your gender is {gender} and your age is: {age}")
        choice = input("Are there more people? type 'y' for yes and 'n' for no: ").lower()
        if choice == 'y':
            continue
        else:
            should_continue = False

play_game()