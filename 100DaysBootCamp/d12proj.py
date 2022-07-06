
# Choosing a random number between 1 and 100
# Function to check user's guess agains actual answer

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, correct_answer, turns):
    """Check answer against guess. Returns the number of turns remaining."""
    if user_guess > correct_answer:
        print("Too high")
        return turns-1
    elif user_guess < correct_answer:
        print("Too low")
        return turns-1
    else:
        print(f"You got it. The answer was {correct_answer}")

# Make a function to set difficulty


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' ")
    if level == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def game():

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1, 100)
    print(f"The correct answer is {answer}")

    # Let the user guess a number
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != answer:
            print("Guess Again!")


game()
# Track the number of turns and reduce by 1 if they get it wrong

# Repeat
