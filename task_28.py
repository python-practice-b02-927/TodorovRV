#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    if cell_is_filled():
        a = 1
    else:
        a = 0
    while True:
        move_right()
        if cell_is_filled():
            a += 1
        if a == 5:
            break

if __name__ == '__main__':
    run_tasks()
