#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():  
    move_right(2)
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    paint_right()
    paint_down()
    move_left()
    fill_cell()
    move_up()


def paint_right():
    move_right()
    fill_cell()
    move_left()

        
def paint_down():
     move_down()
     fill_cell()
     move_up()  



if __name__ == '__main__':
    run_tasks()
