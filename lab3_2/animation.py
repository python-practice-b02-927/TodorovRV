import graphics as g
import math as m
import random as ran


n = int(input())
r = 5
# dt - time interval between frames
dt = 1
# accel = acceleration
accel0 = 1000
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
def object_movement(r):
    objects(n)
    stop = 0
    while True:
        for i in range(n):
            if x[i] <= 500 and y[i] <= 500:
                dx = vel[i] * m.sin(alpha[i]) * dt
                dy = vel[i] * m.cos(alpha[i]) * dt
                if (x[i] + dx) < (500 - r * m.sin(alpha[i])):
                    x[i] += dx
                    y[i] += dy
                    object[i].move(dx, dy)
                    accel = accel0 / ((500 - x[i]) ** 2 + (500 - y[i]) ** 2)
                    vel[i] += accel * dt
                else:
                    if st[i] == 1:
                        continue
                    r += 1
                    star(r)
                    stop += 1
                    st[i] = 1
                    object[i].move(500 - x[i], 500 - y[i])

            if x[i] >= 500 and y[i] >= 500:
                dx = vel[i] * m.sin(alpha[i]) * dt
                dy = vel[i] * m.cos(alpha[i]) * dt
                if (x[i] - dx) > (500 + r * m.sin(alpha[i])):
                    x[i] -= dx
                    y[i] -= dy
                    object[i].move(-dx, -dy)
                    accel = accel0 / ((-500 + x[i]) ** 2 + (-500 + y[i]) ** 2)
                    vel[i] += accel * dt
                else:
                    if st[i] == 1:
                        continue
                    r += 1
                    star(r)
                    stop += 1
                    st[i] = 1
                    object[i].move(500 - x[i], 500 - y[i])

            if x[i] < 500 and y[i] > 500:
                dx = vel[i] * m.sin(alpha[i]) * dt
                dy = vel[i] * m.cos(alpha[i]) * dt
                if (x[i] + dx) < (500 - r * m.sin(alpha[i])):
                    x[i] += dx
                    y[i] -= dy
                    object[i].move(dx, -dy)
                    accel = accel0 / ((-500 + x[i]) ** 2 + (-500 + y[i]) ** 2)
                    vel[i] += accel * dt
                else:
                    if st[i] == 1:
                        continue
                    r += 1
                    star(r)
                    stop += 1
                    st[i] = 1
                    object[i].move(500 - x[i], 500 - y[i])

            if x[i] > 500 and y[i] < 500:
                dx = vel[i] * m.sin(alpha[i]) * dt
                dy = vel[i] * m.cos(alpha[i]) * dt
                if (x[i] - dx) > (500 + r * m.sin(alpha[i])):
                    x[i] -= dx
                    y[i] += dy
                    object[i].move(-dx, dy)
                    accel = accel0 / ((-500 + x[i]) ** 2 + (-500 + y[i]) ** 2)
                    vel[i] += accel * dt
                else:
                    if st[i] == 1:
                        continue
                    r += 1
                    star(r)
                    stop += 1
                    st[i] = 1
                    object[i].move(500 - x[i], 500 - y[i])
        g.time.sleep(0.0005)
        if stop == n:
            break
    return r


"""this function draw star explosion"""
def boom(r):
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
    r1 = object_movement(r)
    g.time.sleep(3)
    boom(r1)


main()

