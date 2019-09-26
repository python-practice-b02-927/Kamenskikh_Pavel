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


def draw_background():
    pass


def draw_ball():
    pass


def draw_sun():
    pass


def draw_cloud():
    pass


def draw_fish():
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


def decoration():
    draw_background()
    draw_sun()
    draw_cloud()
    draw_ball()


def move():
    pass


def main():
    move()
    check_walls()
    check_water()
    check_floor()


decoration()

while t <= 100:
    main()
    t += 1