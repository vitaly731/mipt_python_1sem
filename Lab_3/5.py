from random import *
import turtle

number_of_turtles = 60
steps_of_time_number = 1000

turtle.penup()
turtle.goto(-250, -250)
turtle.pendown()
turtle.pensize(3)
for i in range(4):
    turtle.forward(250 * 2)
    turtle.left(90)
turtle.hideturtle()

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shapesize(0.5)
    unit.penup()
    unit.speed("fastest")
    unit.goto(randint(-248, 248), randint(-248, 248))
    unit.left(360 * (random() - 0.5))

for i in range(steps_of_time_number):
    for unit in pool:
        if unit.ycor() <= -248 or unit.ycor() >= 248:
            unit.setheading(360 - unit.heading())
        if unit.xcor() <= -248 or unit.xcor() >= 248:
            unit.setheading(180 - unit.heading())
        unit.forward(4)
