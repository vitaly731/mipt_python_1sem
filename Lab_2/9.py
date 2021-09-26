import turtle as t
import math as m

def drawN(n, R):
    t.penup()
    t.goto(R, 0)
    t.pendown()
    a = 2 * R * m.sin(m.pi / n)
    t.setheading(180 - 90 * (n - 2) / n)
    t.forward(a)
    for i in range(1, n):
        t.left(360 / n)
        t.forward(a)

R = 50
dR = R * 2/3
for n in range(3, 13 + 1):
    drawN(n, R)
    R += dR
