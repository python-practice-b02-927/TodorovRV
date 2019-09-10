import turtle as t

def vka(n):
    t.circle(n * 10)
    t.left(180)
    t.circle(n * 10)

for i in range(10):
    vka(i + 4)
