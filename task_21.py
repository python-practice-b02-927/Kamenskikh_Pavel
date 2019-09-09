#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    def way():
        move_right()
        fill_cell()
    n=1
    move_down()
    while not wall_is_beneath():
        for i in range(n):
            way()
        move_left(n)
        move_down()
        n+=1
    move_right()


if __name__ == '__main__':
    run_tasks()
