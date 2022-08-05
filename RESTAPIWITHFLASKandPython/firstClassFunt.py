def divide(dividend, divisor):
    if not divisor:
        raise ZeroDivisionError("Divisor can be 0")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(30, 12, operator=divide)
#print(result)

def search(sequnce, expected, finder):
    for item in sequnce:
        if finder(item) == expected:
            return item
    raise RecursionError(f"Could not find an element with {expected}")


from operator import itemgetter

friends = [
    {"name": "Rolf Smith", "age":24},
    {"name": "Adam Wool", "age":30},
    {"name": "Anne Pun", "age":27}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", itemgetter("name")))


