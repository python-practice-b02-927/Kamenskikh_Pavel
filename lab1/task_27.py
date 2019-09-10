#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    n=0
    move_right()
    fill_cell()
    while True:
        for i in range(n):
            if not wall_is_on_the_right():
                move_right()
            else:
                break
        if wall_is_on_the_right():
            break
        fill_cell()
        n+=1
               


if __name__ == '__main__':
    run_tasks()
