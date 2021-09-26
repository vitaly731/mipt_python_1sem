import turtle as t
import time

t.speed('fast')

def star(n, b):
    a = 200
    t.forward(a)
    for i in range(1, n):
        t.left(180 - 180 / n)
        t.forward(a)

k = 5
star(k, 200)
time.sleep(3.5)
t.clear()
k = 11
star(k, 200)
