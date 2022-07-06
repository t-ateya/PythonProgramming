from urllib import response
from d14_art import logo, vs
from d14_game_data import data
import random
from replit import clear
# Format the account data into printable data


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description}, {account_country}"


def check_answer(guess, a_follower_count, b_follower_count):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


# Display art

def play_game():

    score = 0
    game_should_continue = True
    account_b = random.choice(data)
    while game_should_continue:

        # Generate a random account from the game data
        account_a = account_b
        account_b = random.choice(data)
        # if account_a == account_b:
        while account_a == account_b:

            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        # Ask user for a guess

        guess = input("Who has more follower? Type 'A' or 'B': ").lower()

        # Check if user is correct

        # Get follower count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        # Use if statement to check if user is correct

        # clear the screen between rounds
        clear()
        print(logo)
        # Give user feedback on their guess
        if is_correct:
            score += 1
            print(f"You're  right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry!!!, That's wrong!. Final score: {score}")

    # Make the guess repeatable

    # Making account at position B to become the next account at position A

    # Clear the screen
play_game()
