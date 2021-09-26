import turtle as t

t.speed(10)

radius_increment = 13
radius = 20
for i in range(10):
    t.setheading(90)
    t.circle(radius)
    t.circle(-radius)
    radius += radius_increment
