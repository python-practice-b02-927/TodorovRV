import graphics as g
import math as m
import random as ran


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


def coords():
    n = int(input())
    for i in range(n):
        x.append(0)
        y.append(0)
        alpha.append(0)
        vel.append(0)
        x[i] = int(ran.randint(1, 1000))
        y[i] = int(ran.randint(1, 1000))
        object.append(0)
        st.append(0)


def star(r):
    star = g.Circle(g.Point(500, 500), r)
    star.setFill('yellow')
    star.draw(w)


def object_movement():
    pass


def boom():
    pass


def main():
    coords()
    star(r)
    object_movement()
    g.time.sleep(3)
    boom()


main()

