import graphics as gr
import math

from math import sin, pi, cos

SIZE_X = 800
SIZE_Y = 600

w = gr.GraphWin("Resistance", SIZE_X, SIZE_Y)
t = 1
k1 = 0.01
k2 = 0.1
Velocity = 10
a = pi/3

coords = gr.Point(100, 500)
velocity = gr.Point(Velocity*cos(a), Velocity*sin(a))

acceleration_g = 10
acceleration_k = gr.Point(0, 0)


def draw_background(w):
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y * 1 / 2))
    sky.setFill('LightSkyBlue')
    sky.setOutline('LightSkyBlue')
    sea = gr.Rectangle(gr.Point(0, SIZE_Y * 1 / 2), gr.Point(SIZE_X, SIZE_Y*11/12))
    sea.setFill('Navy')
    sea.setOutline('Navy')
    sand = gr.Rectangle(gr.Point(0, SIZE_Y * 11/12), gr.Point(SIZE_X, SIZE_Y))
    sand.setFill('yellow4')
    sand.setOutline('yellow4')

    sky.draw(w)
    sea.draw(w)
    sand.draw(w)
    raft(0, SIZE_Y/2)
    raft(SIZE_X/8, SIZE_Y/2)


def draw_ball(w):
    pass


def raft(x, y):
    pass


def draw_sun(w):
    pass


def draw_cloud(w):
    pass


def draw_fish(w):
    pass


def update_velocity():
    pass


def update_acceleration():
    pass


def check_water():
    pass


def check_walls():
    pass


def check_floor():
    pass


def decoration(w):
    draw_background(w)
    draw_sun(w)
    draw_cloud(w)
    draw_ball(w)


def move():
    pass


def main(t):
    decoration(w)
    while t <= 100:
        move()
        check_walls()
        check_water()
        check_floor()
        t += 1


main(t)

w.getMouse()
w.close()
