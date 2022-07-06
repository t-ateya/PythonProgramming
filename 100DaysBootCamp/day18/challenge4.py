import turtle as t
import random as r

tim = t.Turtle()
colors = ["dark blue", "cornflower blue", "indigo", "magenta", "blue", "red"]
directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(r.choice(colors))
    tim.forward(30)
    tim.setheading(r.choice(directions))