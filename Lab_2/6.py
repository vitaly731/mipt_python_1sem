import turtle as t

t.shape("turtle")

n = int(input("Enter a number of spider's paws: "))
for i in range(1, n + 1):
    t.right(360 / n)
    t.forward(100)
    t.stamp()
    t.right(180)
    t.forward(100)
    t.right(180)
