#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    a = 0
    if wall_is_above() and wall_is_beneath:
        fill_cell()
    while  wall_is_beneath():
        move_right()
        if wall_is_above() and wall_is_beneath:
            fill_cell()
        if (not wall_is_above()) and wall_is_beneath():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    a += 1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
    
    mov ('ax',a) 

if __name__ == '__main__':
    run_tasks()
