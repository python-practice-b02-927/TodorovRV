import turtle

i = 0
j = 0
for j in range(10):
    for i in range(4):
        turtle.forward(j * 10)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.backward(5)
    turtle.pendown()