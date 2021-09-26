import turtle as t

for i in range(1, 10 + 1):
    t.forward(15 * i)
    for j in range(3):
        t.left(90)
        t.forward(15 * i)
    t.right(90)
    t.penup()
    t.forward(7)
    t.left(90)
    t.forward(7)
    t.left(90)
    t.pendown()
    
    
        
