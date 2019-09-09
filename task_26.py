#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    for i in range(4):
        for j in range(9):
            krest()
            move_right(n = 4)
        krest()
        move_down(n=4)
        while not wall_is_on_the_left():
            move_left()
    for j in range(9):
        krest()
        move_right(n = 4)
    krest()
    while not wall_is_on_the_left():
        move_left()
def krest():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_left()
    fill_cell()
    move_right(n=2)
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_up(n=2)
    move_left()
if __name__ == '__main__':
    run_tasks()
