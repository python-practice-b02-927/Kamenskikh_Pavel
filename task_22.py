#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    
    def paint_line():
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        fill_cell()
        while not wall_is_on_the_left():
            move_left()    
    while not wall_is_beneath():
        paint_line()
        move_down()
        
    paint_line()


if __name__ == '__main__':
    run_tasks()
