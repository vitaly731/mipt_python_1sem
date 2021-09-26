import turtle as t

t.shape("circle")

g = 9.81
ay = -g
dt = 0.01
vx = 39
vy = 70
k = 0.6
x = -700.0
y = 0.0
t.penup()
t.goto(x, y)
t.pendown()

for i in range(10000):
    if i != 0 and y <=-1:
        vx *= k
        vy *= -k
    x += vx * dt
    y += vy * dt + ay * dt ** 2 / 2
    t.goto(x, y)
    vy += ay * dt
    
        
