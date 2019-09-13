#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while not wall_is_on_the_left():
        move_left()
    while True:
        if wall_is_above() and wall_is_beneath():
            move_right()
        else:
            home()
            break



def home():
    if not wall_is_above():
        move_up()
    else:
        move_down()
    while not wall_is_on_the_left():
        move_left() 
    while not wall_is_above():
        move_up()
               


if __name__ == '__main__':
    run_tasks()
