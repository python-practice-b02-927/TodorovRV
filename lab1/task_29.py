#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    if cell_is_filled():
        a = 1
    else:
        a = 0
    while not wall_is_on_the_right():
        move_right()
        if cell_is_filled():
            a += 1
        if a == 3:
            break
        if not cell_is_filled():
            a = 0


if __name__ == '__main__':
    run_tasks()
