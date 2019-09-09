#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    for i in range(4):
        krest()
        move_right(n=4)
        move_up()
    krest()
def krest():
    move_right()
    move_down()
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
