from replit import clear

from art9 import logo
# print(logo)


# Trial solution

def get_input():
    name = input("What is your name?: \n")
    bid_price = input("What is your bid?: \n")
    return name, bid_price


def secret_auction():
    auction = {}
    name, bid = get_input()
    auction["name"] = name
    auction["bid"] = bid
    response = input("Are they other users who want to bid? 'yes' or 'no' ?\n")
    if response == "yes":
        clear()
        new_auction = {}
        name, bid = get_input()
        new_auction["name"] = name
        new_auction["bid"] = bid
        auction.update(new_auction)
        print(auction)
    else:
        print("Finding the highest bid in the dic")
    print(auction)


# secret_auction()


# Correct Solution
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid_price = 0
    winner = ""
    for bidder in bidding_record:
        bid_value = bidding_record[bidder]
        if bid_value > highest_bid_price:
            highest_bid_price = bid_value
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid_price}")


print(logo)
print("Welcome to the secret auction program.")
while not bidding_finished:
    name = input("What is your name?\n")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders?  Type 'yes' or 'no' \n")
    if should_continue.lower() == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue.lower() == "yes":
        clear()
