
from turtle import Turtle, Screen
timmy = Turtle()

#print(timmy.fd)

#my_screen = Screen()
#print(my_screen.canvheight)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("My best names", ["Joyces", "ateya", "arrey", "JC", "Success"])
table.add_column("Carreer Choice", ["Law","Engineering", "Medicine", "Medicine", "Engineering"])
table.align = "l"
print(table)