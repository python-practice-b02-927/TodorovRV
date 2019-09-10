import turtle as t
import math as m
def krug(n):
    t.left(90 + 180 / n)
    for i in range (n):
        t.forward(n * 5)
        t.left(360 / n)
    t.right(90 + 180 / n)

for i in range (10):
    krug(i + 3)
    t.penup()
    t.forward(((i + 4) * 5 / 2 / m.sin(2*3.1415/ 2 / (i + 4))) - ((i + 3) * 5 / 2 / m.sin(2*3.1415/ 2 / (i + 3))))
    t.pendown()
