import turtle as t
import math

step = 40
steprt = step * math.sqrt(2)

def draw1():
    t.penup()
    t.forward(step)
    t.pendown()
    t.penup()
    t.right(90)
    t.forward(step)
    t.pendown()
    t.left(135)
    t.forward(steprt)
    t.right(135)
    t.forward(2 * step)
    t.penup()
    t.left(180)
    t.forward(2 * step)
    t.right(90)

def draw4():
    t.penup()
    t.forward(step)
    t.pendown()
    t.right(90)
    t.forward(step)
    t.left(90)
    t.forward(step)
    t.left(90)
    t.forward(step)
    t.left(180)
    t.forward(2 * step)
    t.left(180)
    t.forward(2 * step)
    t.penup()
    t.right(90)

def draw7():
    t.penup()
    t.forward(step)
    t.pendown()
    t.forward(step)
    t.right(135)
    t.forward(steprt)
    t.left(45)
    t.forward(step)
    t.left(180)
    t.forward(step)
    t.right(45)
    t.forward(steprt)
    t.right(45)

def draw0():
    t.penup()
    t.forward(step)
    t.pendown()
    t.right(90)
    t.forward(2 * step)
    t.left(90)
    t.forward(step)
    t.left(90)
    t.forward(2 * step)
    t.left(90)
    t.forward(step)
    t.left(180)
    t.forward(step)

draw1()
draw4()
draw1()
draw7()
draw0()
draw0()

