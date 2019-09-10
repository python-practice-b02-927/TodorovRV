#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    a = 0
    while a < 3:
        while not wall_is_on_the_left():
            move_left()
            if not wall_is_beneath():
                a = 0
                while not wall_is_beneath():
                    move_down()
                break
        while not wall_is_on_the_right():
            move_right()
        a += 1
    while not wall_is_on_the_left():
            move_left()
if __name__ == '__main__':
    run_tasks()
