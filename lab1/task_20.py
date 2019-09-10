#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for j in range(6):
        for i in range(27):
            move_right()
            fill_cell()
        move_down()
        fill_cell()
        for i in range(26):
            move_left()
            fill_cell()
        move_left()
        move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()
