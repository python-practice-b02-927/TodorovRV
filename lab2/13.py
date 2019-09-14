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


def eye():
    t.color("blue")
    cir(20)


def face():
    t.color("yellow")
    cir(100)


def moving1():
    t.penup()
    t.left(90)
    t.forward(170)
    t.left(90)
    t.forward(30)
    t.pendown()


def eyes():
    eye()
    t.penup()
    t.backward(60)
    t.pendown()
    eye()


def moving2():
    t.penup()
    t.forward(30)
    t.left(90)
    t.forward(60)


def nose():
    t.width(3)
    t.pendown()
    t.forward(20)
    t.width(1)


def moving3():
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()


def smile():
    t.width(3)
    t.color("red")
    duga(1.9)
    t.width(1)


face()
moving1()
eyes()
moving2()
nose()
moving3()
smile()


