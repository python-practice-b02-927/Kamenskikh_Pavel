#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    move_down()
    for i in range(4):
        crossline()
        move_down(4)
    crossline()
    move_up()


def paint_right():
    move_right()
    fill_cell()


def paint_down():
    move_down()
    fill_cell()
    move_up()

    
def paint_up():
    move_up()
    fill_cell()
    move_down()

    
def cross():
    fill_cell()
    move_right()
    fill_cell()
    paint_up()
    paint_down()
    paint_right()

    
def crossline():
    for i in range(9):
        cross()
        move_right(2)
    cross()
    while not wall_is_on_the_left():
        move_left()



if __name__ == '__main__':
    run_tasks()
