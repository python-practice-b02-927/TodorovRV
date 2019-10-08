from tkinter import *
from random import randrange as rnd, choice
import time
import math as m
root = Tk()
root.geometry('800x600')

ball = []
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
l = Label(bg='black', fg='white', width=20)
score = 0
l.pack()

colors = ['red','orange','yellow','green','blue']
def new_ball():
    global ball
    ball.append({'id' : 0, 'x' : rnd(100,700), 'y' : rnd(100,500), 'r' : rnd(30,50), 'vx' : rnd(-4, 4), 'vy' : rnd(-4, 4)})
    ball[len(ball) - 1]['id'] = canv.create_oval(ball[len(ball) - 1]['x'] - ball[len(ball) - 1 ]['r'],ball[len(ball) - 1]['y'] -
                                           ball[len(ball) - 1]['r'],ball[len(ball) - 1]['x'] + ball[len(ball) - 1]['r'],
                                           ball[len(ball) - 1]['y'] + ball[len(ball) - 1]['r'],fill = choice(colors), width=0)
    root.after(450, new_ball)
    if len(ball) > 4:
        canv.delete(ball[0]['id'])
        del ball[0]


def click(event):
    global ball, score
    x0 = event.x
    y0 = event.y
    for i in range(len(ball) - 1):
        if (m.fabs(x0 - ball[i]['x']) < ball[i]['r']) & (m.fabs(y0 - ball[i]['y']) < ball[i]['r']):
            score += m.floor(ball[i]['r'] / (m.floor(m.fabs(x0 - ball[i]['x'])**2) + 1 +
                                             m.floor((m.fabs(y0 - ball[i]['y'])) ** 2)) * 100)
            l['text'] = 'Score: ' + str(score)
            canv.delete(ball[i]['id'])
            del ball[i]


def movement():
    global ball
    for i in range(len(ball) - 1):
        if (ball[i]['x'] + ball[i]['vx'] > 800) | (ball[i]['x'] + ball[i]['vx'] < 0):
            ball[i]['vx'] = -ball[i]['vx']
        if(ball[i]['y'] + ball[i]['vy'] > 600) | (ball[i]['y'] + ball[i]['vy'] < 0):
            ball[i]['vy'] = -ball[i]['vy']
        ball[i]['x'] += ball[i]['vx']
        ball[i]['y'] += ball[i]['vy']
        canv.delete(ball[i]['id'])
        ball[i]['id'] = canv.create_oval(ball[i]['x'] - ball[i]['r'], ball[i]['y'] - ball[i]['r'],
                                                     ball[i]['x'] + ball[i]['r'],ball[i]['y'] + ball[i]['r'],
                                                     fill=choice(colors), width=0)
    root.after(5, movement)

new_ball()
movement()
canv.bind('<Button-1>', click)
mainloop()