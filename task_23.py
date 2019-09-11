#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():   
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_above():
            paint_up()
    while wall_is_beneath():
        move_left()


def paint_up():
    while not wall_is_above():
        move_up()
        fill_cell()
    while not wall_is_beneath():
        move_down()
    
            


if __name__ == '__main__':
    run_tasks()
