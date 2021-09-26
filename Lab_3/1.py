from random import *
import turtle as t

n = int(input())
for i in range(n):
    t.left((random() - 0.5) * 360)
    t.forward(random() * 80)
    
    
