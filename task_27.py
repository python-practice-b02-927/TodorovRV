#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    a = 1;
    move_right()
    fill_cell()
    while True:
        for i in range(a):
            if wall_is_on_the_right():
                break
            else:
                move_right()
        if wall_is_on_the_right():
            break
        a += 1;
        fill_cell()


if __name__ == '__main__':
    run_tasks()
