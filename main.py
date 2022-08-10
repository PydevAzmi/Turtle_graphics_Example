from turtle import Turtle, Screen
import random
import numpy as np

hel = Turtle()
# hel.setposition(-100, 150)
hel.pensize(4)
hel.speed(0.1)
hel.shape("circle")
move = [0, 90, 180, 270]
for i in range(100):
    color_ = list(np.random.choice(range(0, 2), size=3))
    hel.setheading(random.choice(move))
    hel.forward(20)
    rgb = (color_[0] / 3, color_[1] / 2, color_[2])
    hel.color(rgb)

screen = Screen()
screen.exitonclick()

# for i in range(3, 10, 1):
#     color_ = list(np.random.choice(range(0, 2), size=3))
#     rgb = (color_[0]/3, color_[1]/2, color_[2])
#     hel.pencolor(rgb)
#     hel.fillcolor(rgb)
#     for l_ in range(i):
#         hel.forward(150)
#         hel.right(360 / i)
