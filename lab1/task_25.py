#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down(2)                
    for i in range(4):
        cross()
        move_right(2)
    cross()
    move_left(2)
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
    

if __name__ == '__main__':
    run_tasks()
