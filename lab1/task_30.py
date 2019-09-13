#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    n=0
    move_right()
    while not wall_is_on_the_right():
        move_right()
        n+=1
    while not wall_is_on_the_left():
        move_left()
    while n>=0:
        square(n)
        n-=2
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()


def square(k):
    move_right()
    for i in range(k):
        fill_cell()
        move_right()
    move_down()
    for i in range(k):
        fill_cell()
        move_down()
    move_left()
    for i in range(k):
        fill_cell()
        move_left()
    move_up()
    for i in range(k):
        fill_cell()
        move_up()
    move_down()
    move_right()

    
if __name__ == '__main__':
    run_tasks()
