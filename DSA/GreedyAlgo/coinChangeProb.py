"""
    You are given coins of different denominations and total amount of money. Find the minimum number of coins that you need to make up the given amount

    Solution-Algo
    - Find the biggest coin that is less than the given total number
    - Add coin to the result and subtract that coin from the total number

    If V is equal to zero:
        Then print result
    else:
        Repeat step 2 and 3

"""

def coin_change(total_number, coins):
    result = []
    N = total_number
    coins.sort()
    index = len(coins) -1 
    while True:
        coin_value = coins[index]
        if coin_value <= N:
            result.append(coin_value)
            #print(coin_value)
            N = N - coin_value
        if N < coin_value:
            index -=1
        if N == 0:
            break 
    return result

coins = [1, 2, 5, 20, 50, 200]
print(coin_change(201, coins))