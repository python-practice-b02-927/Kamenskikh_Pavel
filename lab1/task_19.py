#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    def home():
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()
    while wall_is_above() and wall_is_beneath() and not wall_is_on_the_left():
        move_left()
    if not wall_is_above():
        home()
    else:
            while wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
                move_right()
            if not wall_is_above():
                home()
            


if __name__ == '__main__':
    run_tasks()
