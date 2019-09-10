import turtle as t

def star(n):
    for i in range (n):
        t.forward(100)
        t.left(180 - (180 / n))

star(5)
t.penup()
t.forward(250)
t.pendown()
star(11)