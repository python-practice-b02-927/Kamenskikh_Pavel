#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():        
    if wall_is_above():
        if wall_is_on_the_left():
            slide_right()
            slide_down()
        else:
            slide_down()
            slide_left()
    else:
        if wall_is_on_the_left():
            slide_right()
            slide_up()
        else:
            slide_left()
            slide_up()


def slide_right():
    while not wall_is_on_the_right():
        move_right()

        
def slide_left():
    while not wall_is_on_the_left():
        move_left()

        
def slide_up():
    while not wall_is_above():
        move_up()

        
def slide_down():
    while not wall_is_beneath():
        move_down()
        


if __name__ == '__main__':
    run_tasks()
