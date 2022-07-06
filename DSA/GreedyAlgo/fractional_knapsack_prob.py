"""
    Fractional Knapsack Problem

    Given a set of items, each with weight and a value, determine the number of each item to include in a collection so that 
    the total weight is less than or equal to a given limit and the total value is as large as possible.

    Algorithm
    -Calculate the density or ratio for each item
    - Sort items based on this ratio
    - Take items with the highest ratio sequentially until weight allows
    - Add the next item as much (fractional) as we can
"""


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value 
        self.ratio = value / weight

def knapsack_method(items, capacity):
    items.sort(key=lambda item:item.ratio, reverse = True )
    used_capacity = 0
    total_value = 0

    for item in items:
        if used_capacity + item.weight <= capacity:
            used_capacity += item.weight
            total_value += item.value
        else:
            unused_weight = capacity - used_capacity
            value = item.ratio*unused_weight
            used_capacity += unused_weight
            total_value += value 

        if used_capacity == capacity:
            break 
    print("Total value obtained: " + str(total_value))

item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)

cList = [item1, item2, item3]

knapsack_method(cList, 50)
    
