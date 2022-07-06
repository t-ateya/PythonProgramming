# Global Scope
play_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(play_health)
    drink_potion()

# print(play_health)


# No block scope in python

"""
game_level = 3
enemies = ["Skeleton", "Zombie", "Alie"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
"""

# Modifying a global scope
enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@t_ateya"
