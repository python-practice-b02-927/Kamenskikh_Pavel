#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    def home():
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            move_right()
        else:
            home()
    if not wall_is_above():
        home()
    while not wall_is_on_the_left():
        if wall_is_above() and wall_is_beneath():
            move_left()
        else:
            home()
    if not wall_is_above():
        home()
            


if __name__ == '__main__':
    run_tasks()
