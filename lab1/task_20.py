#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_down(1)

    while not wall_is_beneath():
        move_up(1)
        snake()
    move_up()
    move_right()
    
    
def snake():
    move_right()
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
    move_down()
    move_left()
    while not wall_is_on_the_left():
        fill_cell()
        move_left()
    move_down(2)      

if __name__ == '__main__':
    run_tasks()
