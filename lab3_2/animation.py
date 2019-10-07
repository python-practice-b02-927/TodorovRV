import graphics as g
import math as m
import random as ran


n = int(input())
r = 5
# st - object status: 1 - object have fallen on star, 0 - object falling on star
st = []
x = []
y = []
# alpha - angle between direction to object and horizontal line
alpha = []
# vel = velocity
vel = []
object = []
w = g.GraphWin("Model", 1000, 1000)


"""this function get coordinates of objects"""
def coords():
    for i in range(n):
        x.append(0)
        y.append(0)
        alpha.append(0)
        vel.append(0)
        x[i] = int(ran.randint(1, 1000))
        y[i] = int(ran.randint(1, 1000))
        object.append(0)
        st.append(0)


"""this function draw star"""
def star(r):
    star = g.Circle(g.Point(500, 500), r)
    star.setFill('yellow')
    star.draw(w)


"""this function draw objects"""
def objects(n):
    for i in range(n):
        object[i] = g.Circle(g.Point(x[i], y[i]), 2)
        object[i].setFill('brown')
        object[i].draw(w)
        if y[i] != 500:
            alpha[i] = abs(m.atan(((500 - x[i]) / (500 - y[i]))))
        else:
            alpha[i] = abs(m.atan(((500 - x[i]) / 0.00000001)))


"""this function move objects"""
def object_movement():
    objects(n)


"""this function draw star explosion"""
def boom():
    for i in range(100):
        star = g.Circle(g.Point(500, 500), (r + i))
        star.setFill('orange')
        star.draw(w)
        g.time.sleep(0.00001)
    for j in range(600):
        star = g.Circle(g.Point(500, 500), (r + i + j))
        star.setFill('red')
        star.draw(w)
        g.time.sleep(0.00001)


def main():
    coords()
    star(r)
    object_movement()
    g.time.sleep(3)
    boom()


main()

