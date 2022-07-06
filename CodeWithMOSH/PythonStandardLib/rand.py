import random
import string

# This module generates a random value b/t 0 and 1
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print("".join(random.choices("abcdefghijkel", k=4)))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))
