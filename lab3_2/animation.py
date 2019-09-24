import graphics as g
import math as m

dt = 0.2
r = 5
n = 1
i = 0
SIZE_X = 1000
SIZE_Y = 1000
L = []
T = ()

L.append(1)
L.append('abx')
t = tuple(L)
x = []
y = []
a = []
v = []
ob = []
accel = 1
w = g.GraphWin("Model", SIZE_X, SIZE_Y)


def coords():
    for i in range(n):
        x.append(0)
        y.append(0)
        a.append(0)
        v.append(0)
        x[i] = int(input())
        y[i] = int(input())
        ob.append(0)


def star(r):
    star = g.Circle(g.Point(500, 500), r)
    star.setFill('yellow')
    star.draw(w)


def obj(r):
    for i in range(n):
        ob[i] = g.Circle(g.Point(x[i], y[i]), 2)
        ob[i].setFill('yellow')
        ob[i].draw(w)
        a[i] = m.atan((x[i]/y[i]))

    while True:
        for i in range(n):
            dx = v[i] * m.sin(a[i]) * dt
            dy = v[i] * m.cos(a[i]) * dt
            if (x[i] - dx) < (500 - r*m.cos(a[i])):
                x[i] -= dx
                y[i] -= dy
                ob[i].move(dx, dy)
                v[i] += accel * dt
            else:
                r += 20
                star(r)
        g.time.sleep(0.05)


def main():
    coords()
    star(r)
    obj(r)


main()

