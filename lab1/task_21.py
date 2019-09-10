#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    a = 1
    for i in range(13):
        move_down()
        for j in range(a):
            move_right()
            fill_cell()
        for j in range(a):
            move_left()
        a += 1;
    move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()
