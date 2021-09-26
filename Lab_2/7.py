import turtle as t
import math

t.speed("fastest")

step = 60
Phi = 0
dt = 0.01
dPhi = dt

for i in range(3000):
    Phi += dPhi
    t.goto(step/(2*math.pi) * Phi * math.cos(Phi), step/(2*math.pi) * Phi * math.sin(Phi)) 

