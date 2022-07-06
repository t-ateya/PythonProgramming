
from turtle import  Turtle, Screen
import random

tim = Turtle()
tim2 = Turtle()

"""
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

"""
"""
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)

for _ in range(4):
    tim.forward(100)
    tim.left(90)


tim2.forward(300)
tim2.left(45)
tim2.left(45)

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

"""



"""

colors = ["dark blue", "cornflower blue", "indigo", "magenta", "blue", "red"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

"""

#draw_shap(10)



#Challenge4




screen = Screen()
screen.exitonclick()