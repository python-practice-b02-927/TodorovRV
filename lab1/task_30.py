#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    a = 1
    while not wall_is_on_the_right():
        move_right()
        a += 1
    b = a
    while not wall_is_on_the_left():
        move_left()
    b -= 2
    while b > 0:
        for i in range(b):
            move_right()
            fill_cell()
        for i in range(b - 1):
            move_left()
        move_down()
        b -= 2
    b = a
    b -= 2
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_above():
        move_up()
    while b > 0:
        for i in range(b):
            move_down()
            fill_cell()
        for i in range(b - 1):
            move_up()
        move_right()
        b -= 2
    b = a
    b -= 2
    while not wall_is_on_the_right():
        move_right()
    while not wall_is_above():
        move_up()
    while b > 0:
        for i in range(b):
            move_down()
            fill_cell()
        for i in range(b - 1):
            move_up()
        move_left()
        b -= 2
    b = a
    b -= 2
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()
    while b > 0:
        for i in range(b):
            move_right()
            fill_cell()
        for i in range(b - 1):
            move_left()
        move_up()
        b -= 2
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()
if __name__ == '__main__':
    run_tasks()
