import turtle as t

R = 150
r = 20

t.speed("fast")
t.shape("turtle")
t.pen(fillcolor="black", pensize=3)

t.fillcolor("yellow")
t.begin_fill()
t.circle(R)
t.end_fill()

t.penup()
t.goto(-R/3, 2*R*2/3 - r)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.circle(r)
t.end_fill()

t.penup()
t.goto(+R/3, 2*R*2/3 - r)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.circle(r)
t.end_fill()

t.penup()
t.goto(0, R*5/4)
t.pendown()
t.right(90)
t.forward(R*3/7)

t.penup()
t.left(90)
t.forward(R*3/5)
t.pendown()
t.left(90)
t.circle(R*3/5, -180)



