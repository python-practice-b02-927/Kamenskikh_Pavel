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

coords = gr.Point(100, 280)
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
    draw_raft(0)
    draw_raft(SIZE_X*6/8)


def draw_ball(w):
    ball = gr.Circle(coords, 20)
    ball.setFill('Red')
    ball.setOutline('Red')

    ball.draw(w)


def draw_raft(x):
    raft = gr.Rectangle(gr.Point(x, SIZE_Y/2 - 10), gr.Point(x+200, SIZE_Y/2+20))
    raft.setFill('Brown')
    raft.setOutline('Brown')

    for i in range(5):
        draw_log(40*i+20+x)
    raft.draw(w)


def draw_log(x):
    log = gr.Circle(gr.Point(x, SIZE_Y/2+40), 20)
    log.setFill('Sienna3')
    log.setOutline('Brown')

    log.draw(w)

def draw_sun(w):
    sun = gr.Circle(gr.Point(740, 60), 60)
    sun.setFill("Yellow")
    sun.setOutline('Orange')

    sun.draw(w)


def draw_cloud(x, y):
    for i in range(4):
        part_of_cloud(x+i*30, y, 15)
        part_of_cloud(x+i*30 + 15, y+15, 20)
        part_of_cloud(x+i*30 + 15, y-15, 20)
    part_of_cloud(x+120, y, 15)


def part_of_cloud(x, y, r):
    circle = gr.Circle(gr.Point(x, y), r)
    circle.setOutline('White')
    circle.setFill('White')

    circle.draw(w)


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
    draw_cloud(100, 110)
    draw_cloud(50, 40)
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
