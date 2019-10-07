import graphics as g
import math as m
import random as ran


st = []
x = []
y = []
a = []
v = []
ob = []


def coords():
    n = int(input())
    for i in range(n):
        x.append(0)
        y.append(0)
        a.append(0)
        v.append(0)
        x[i] = int(ran.randint(1, 1000))
        y[i] = int(ran.randint(1, 1000))
        ob.append(0)
        st.append(0)


def star():
    pass


def object_movement():
    pass


def boom():
    pass


def main():
    coords()
    star()
    object_movement()
    g.time.sleep(3)
    boom()


main()

