import turtle as t

def cir(n):
    t.begin_fill()
    t.circle(n)
    t.end_fill()
    t.color("black")
    t.circle(n)

def duga(n):
    for i in range (100):
        t.forward(n)
        t.right(1.8)

t.color("yellow")
cir(100)
t.penup()
t.left(90)
t.forward(170)
t.left(90)
t.forward(30)
t.pendown()
t.color("blue")
cir(20)
t.penup()
t.backward(60)
t.pendown()
t.color("blue")
cir(20)
t.penup()
t.forward(30)
t.left(90)
t.forward(60)
t.width(3)
t.pendown()
t.forward(20)
t.penup()
t.forward(10)
t.left(90)
t.forward(60)
t.right(90)
t.color("red")
t.pendown()
duga(1.9)


