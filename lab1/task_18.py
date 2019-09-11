#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while not wall_is_on_the_left():
        if wall_is_above() and wall_is_beneath():
            move_left()
        else:
            home()
    if not wall_is_above or not wall_is_beneath() and not wall_is_on_the_left():
        home()
    while True:
        if wall_is_above() and wall_is_beneath():
            move_right()
        else:
            home()
            break
    if not wall_is_above or not wall_is_beneath() and not wall_is_on_the_left():
        home() 


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
