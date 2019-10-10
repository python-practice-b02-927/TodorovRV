from tkinter import *
from random import randrange as rnd, choice
import json
import math as m

root = Tk()
root.geometry('800x600')

ball = []
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
l = Label(bg='black', fg='white', width=20)
score = 0
ball_number = 0
l.pack()

colors = ['red', 'orange', 'yellow', 'green', 'blue']
shapes = ['square', 'circle']


def new_ball():
    try:
        global ball, ball_number
        ball.append({'id': 0, 'x': rnd(100, 700), 'y': rnd(100, 500), 'r': rnd(30, 50), 'vx': rnd(-4, 4),
                     'vy': rnd(-4, 4), 'color': choice(colors), 'shape': choice(shapes)})
        if ball[len(ball) - 1]['shape'] == 'circle':
            ball[len(ball) - 1]['id'] = canv.create_oval(ball[len(ball) - 1]['x'] - ball[len(ball) - 1]['r'],
                                                         ball[len(ball) - 1]['y'] - ball[len(ball) - 1]['r'],
                                                         ball[len(ball) - 1]['x'] + ball[len(ball) - 1]['r'],
                                                         ball[len(ball) - 1]['y'] + ball[len(ball) - 1]['r'],
                                                         fill=ball[len(ball) - 1]['color'], width=0)
        if ball[len(ball) - 1]['shape'] == 'square':
            ball[len(ball) - 1]['id'] = canv.create_rectangle(ball[len(ball) - 1]['x'] - ball[len(ball) - 1]['r'],
                                                            ball[len(ball) - 1]['y'] - ball[len(ball) - 1]['r'],
                                                            ball[len(ball) - 1]['x'] + ball[len(ball) - 1]['r'],
                                                            ball[len(ball) - 1]['y'] + ball[len(ball) - 1]['r'],
                                                            fill=ball[len(ball) - 1]['color'], width=0)
        if ball_number < 100:
            root.after(450, new_ball)
        else:
            root.destroy()
        if len(ball) > 4:
            canv.delete(ball[0]['id'])
            del ball[0]
        ball_number += 1
    except TclError:
        pass

def click(event):
    global ball, score
    x0 = event.x
    y0 = event.y
    a = len(ball)
    i = 0
    while i < a:
        if ball[i]['shape'] == 'circle':
            if m.fabs(x0 - ball[i]['x']) ** 2 + m.fabs(y0 - ball[i]['y']) ** 2 < ball[i]['r'] ** 2:
                score += m.floor(1 / ball[i]['r'] / (m.floor(m.fabs(x0 - ball[i]['x']) ** 2) + 1 +
                                                 m.floor((m.fabs(y0 - ball[i]['y'])) ** 2)) * 150000)
                l['text'] = 'Score: ' + str(score)
                canv.delete(ball[i]['id'])
                del ball[i]
                a -= 1
                continue
        if ball[i]['shape'] == 'square':
            if (m.fabs(x0 - ball[i]['x']) < ball[i]['r']) & (m.fabs(y0 - ball[i]['y']) < ball[i]['r']):
                score += m.floor(1 / ball[i]['r'] / (m.floor(m.fabs(x0 - ball[i]['x']) ** 2) + 1 +
                                                 m.floor((m.fabs(y0 - ball[i]['y'])) ** 2)) * 75000)
                l['text'] = 'Score: ' + str(score)
                canv.delete(ball[i]['id'])
                del ball[i]
                a -= 1
        i += 1



def movement():
    try:
        global ball, ball_number
        for i in range(len(ball)):
            if (ball[i]['x'] + ball[i]['vx'] > 800) | (ball[i]['x'] + ball[i]['vx'] < 0):
                ball[i]['vx'] = -ball[i]['vx']
            if (ball[i]['y'] + ball[i]['vy'] > 600) | (ball[i]['y'] + ball[i]['vy'] < 0):
                ball[i]['vy'] = -ball[i]['vy']
            ball[i]['x'] += ball[i]['vx']
            ball[i]['y'] += ball[i]['vy']
            canv.delete(ball[i]['id'])
            if ball[i]['shape'] == 'circle':
                ball[i]['id'] = canv.create_oval(ball[i]['x'] - ball[i]['r'], ball[i]['y'] - ball[i]['r'],
                                                 ball[i]['x'] + ball[i]['r'], ball[i]['y'] + ball[i]['r'],
                                                 fill=ball[i]['color'], width=0)
            if ball[i]['shape'] == 'square':
                ball[i]['id'] = canv.create_rectangle(ball[i]['x'] - ball[i]['r'], ball[i]['y'] - ball[i]['r'],
                                                 ball[i]['x'] + ball[i]['r'], ball[i]['y'] + ball[i]['r'],
                                                 fill=ball[i]['color'], width=0)
        if ball_number < 100:
            root.after(5, movement)
    except TclError:
        pass


def results():
    nick = input("Enter you nickname\n")
    with open('Scoretable.json') as f:
        scoretable = json.load(f)
    if nick in scoretable:
        if scoretable[nick] < score:
            scoretable[nick] = score
    else:
        scoretable[nick] = score
    with open('Scoretable.json', 'w') as f:
        json.dump(scoretable, f, indent=1)


new_ball()
movement()
canv.bind('<Button-1>', click)
mainloop()
results()

