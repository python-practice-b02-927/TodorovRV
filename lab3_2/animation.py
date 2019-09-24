import graphics as g
import math as m

dt = 0.2
r = 5
n = 2
i = 0
SIZE_X = 1000
SIZE_Y = 1000
L = []
T = ()
L.append(1)
L.append('abx')
t = tuple(L)
st = []
x = []
y = []
a = []
v = []
ob = []
accel0 = 1000
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
        st.append(0)


def star(r):
    star = g.Circle(g.Point(500, 500), r)
    star.setFill('yellow')
    star.draw(w)


def obj(r):
    stop = 0
    for i in range(n):
        ob[i] = g.Circle(g.Point(x[i], y[i]), 2)
        ob[i].setFill('yellow')
        ob[i].draw(w)
        a[i] = m.atan(((500 - x[i])/(500 - y[i])))

    while True:
        for i in range(n):
            dx = v[i] * m.sin(a[i]) * dt
            dy = v[i] * m.cos(a[i]) * dt
            if (x[i] - dx) < (500 - r*m.sin(a[i])):
                x[i] += dx
                y[i] += dy
                ob[i].move(dx, dy)
                accel = accel0 / ((500 - x[i]) ** 2 + (500 - y[i]) ** 2)
                v[i] += accel * dt
            else:
                if st[i] == 1:
                    continue
                r += 20
                star(r)
                stop += 1
                st[i] = 1
        g.time.sleep(0.0005)
        if stop == n:
            break


def main():
    coords()
    star(r)
    obj(r)
    g.time.sleep(5)


main()

