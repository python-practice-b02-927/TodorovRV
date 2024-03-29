#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    #Движение влево
    while not wall_is_on_the_left():
        move_left()
        if not wall_is_above():
            move_up()
            break
        if not wall_is_beneath():
            move_down()
            break
    #Движение вправо
    if wall_is_on_the_left():
        while not wall_is_on_the_right():
            move_right()
            if not wall_is_above():
                move_up()
                break
            if not wall_is_beneath():
                move_down()
                break
    #Движение в верхний левый угол
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_above():
        move_up()

if __name__ == '__main__':
    run_tasks()
