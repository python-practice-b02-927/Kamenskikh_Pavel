import graphics as gr

from math import sin, pi, cos

SIZE_X = 800
SIZE_Y = 600
w = gr.GraphWin("Resistance", SIZE_X, SIZE_Y)

friction_air = 0.03
friction_water = 0.2

Velocity_ball_0 = 40
coords_ball = gr.Point(100, SIZE_Y / 2 - 20)
alpha = pi/3
velocity_ball = gr.Point(Velocity_ball_0 * cos(alpha),
                         -Velocity_ball_0 * sin(alpha))
acceleration_g = 3
acceleration_k = gr.Point(0, 0)

fish = []
coords_fish = gr.Point(70, 500)
Velocity_fish_0 = 30
velocity_fish = gr.Point(0, 0)


def draw_background(w):
    sky = gr.Rectangle(gr.Point(0, 0),
                       gr.Point(SIZE_X, SIZE_Y * 1 / 2))
    sky.setFill('LightSkyBlue')
    sky.setOutline('LightSkyBlue')

    sea = gr.Rectangle(gr.Point(0, SIZE_Y * 1 / 2),
                       gr.Point(SIZE_X, SIZE_Y * 11 / 12))
    sea.setFill('Navy')
    sea.setOutline('Navy')

    sand = gr.Rectangle(gr.Point(0, SIZE_Y * 11 / 12),
                        gr.Point(SIZE_X, SIZE_Y))
    sand.setFill('yellow4')
    sand.setOutline('yellow4')

    sky.draw(w)
    sea.draw(w)
    sand.draw(w)

    draw_raft(0)
    draw_raft(SIZE_X * 6 / 8)


def draw_raft(x):
    raft = gr.Rectangle(gr.Point(x, SIZE_Y / 2 - 10),
                        gr.Point(x + 200, SIZE_Y / 2 + 20))
    raft.setFill('Brown')
    raft.setOutline('Brown')

    for i in range(5):
        draw_log(40 * i + 20 + x)
    raft.draw(w)


def draw_log(x):
    log = gr.Circle(gr.Point(x, SIZE_Y / 2 + 40), 20)
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
        part_of_cloud(x + i * 30, y, 15)
        part_of_cloud(x + i * 30 + 15, y + 15, 20)
        part_of_cloud(x + i * 30 + 15, y - 15, 20)
    part_of_cloud(x + 120, y, 15)


def part_of_cloud(x, y, r):
    circle = gr.Circle(gr.Point(x, y), r)
    circle.setOutline('White')
    circle.setFill('White')

    circle.draw(w)


def draw_fish(c_fish):
    body_fish(c_fish)
    tail_fish(c_fish)
    fin_fish(c_fish)
    eye_fish(c_fish)


def body_fish(c_fish):
    body = gr.Oval(gr.Point(c_fish.x - 50, c_fish.y - 20),
                   gr.Point(c_fish.x, c_fish.y + 20))
    body.setFill('Green')
    body.setOutline('Green')

    body.draw(w)

    fish.append(body)


def tail_fish(c_fish):
    tail_1 = gr.Polygon(gr.Point(c_fish.x - 50, c_fish.y),
                    gr.Point(c_fish.x - 70, c_fish.y - 20),
                    gr.Point(c_fish.x - 70, c_fish.y + 20))
    tail_1.setOutline('Red')
    tail_1.setFill('Red')

    tail_2 = gr.Oval(gr.Point(c_fish.x - 65, c_fish.y + 20),
                    gr.Point(c_fish.x - 85, c_fish.y - 20))
    tail_2.setFill('Navy')
    tail_2.setOutline('Navy')

    tail_1.draw(w)
    tail_2.draw(w)

    fish.append(tail_1)
    fish.append(tail_2)


def fin_fish(c_fish):
    fin = gr.Polygon(gr.Point(c_fish.x - 30, c_fish.y - 20),
                    gr.Point(c_fish.x - 20, c_fish.y - 20),
                    gr.Point(c_fish.x - 35, c_fish.y - 35))
    fin.setOutline('Red')
    fin.setFill('Red')

    fin.draw(w)

    fish.append(fin)


def eye_fish(c_fish):
    eye1 = gr.Circle(gr.Point(c_fish.x - 10, c_fish.y - 10), 5)
    eye1.setFill('White')

    eye2 = gr.Circle(gr.Point(c_fish.x - 10, c_fish.y - 10), 2)
    eye2.setFill('Black')

    eye1.draw(w)
    eye2.draw(w)

    fish.append(eye1)
    fish.append(eye2)


def update_velocity_ball():
    velocity_ball.x += acceleration_k.x
    velocity_ball.y += acceleration_k.y + acceleration_g


def update_velocity_fish():
    velocity_fish.x = Velocity_fish_0 * (coords_ball.x - coords_fish.x) / ((
            (coords_ball.x - coords_fish.x) ** 2 + (coords_ball.y - coords_fish.y) ** 2) ** (1 / 2))
    velocity_fish.y = Velocity_fish_0 * (coords_ball.y - coords_fish.y) / ((
            (coords_ball.x - coords_fish.x) ** 2 + (coords_ball.y - coords_fish.y) ** 2) ** (1 / 2))


def update_acceleration():
    if coords_ball.y <= SIZE_Y / 2:
        acceleration_k.x = - friction_air * velocity_ball.x
        acceleration_k.y = - friction_air * velocity_ball.y

    elif coords_ball.y >= SIZE_Y / 2 - 20 and coords_ball.x <= SIZE_X * 3 / 4:
        acceleration_k.x = - friction_water * velocity_ball.x
        acceleration_k.y = - friction_water * velocity_ball.y


def stop_ball():
    velocity_ball.x = 0
    velocity_ball.y = 0

    update_acceleration()


def check_raft():
    if coords_ball.y >= SIZE_Y / 2 - 20 and coords_ball.x >= SIZE_X * 3 / 4:
        stop_ball()


def check_walls():
    if coords_ball.x >= SIZE_X:
        velocity_ball.x = -velocity_ball.x
        update_acceleration()

    elif coords_ball.y <= 0:
        velocity_ball.y = -velocity_ball.y
        update_acceleration()


def check_floor():
    if coords_ball.y >= SIZE_Y * 11 / 12 - 20:
        stop_ball()


def decoration(w):
    draw_background(w)

    draw_sun(w)
    draw_cloud(100, 110)
    draw_cloud(50, 40)

    draw_fish(coords_fish)


def remain_background(w):
    r1 = gr.Rectangle(gr.Point(0, SIZE_Y * 11 / 12), gr.Point(SIZE_X, SIZE_Y))
    r1.setOutline('yellow4')
    r1.setFill('yellow4')

    r1.draw(w)

    draw_fish(coords_fish)


def move_ball(ball, colour):
    ball.setFill(colour)
    ball.setOutline(colour)
    ball.move(velocity_ball.x, velocity_ball.y)

    coords_ball.x += velocity_ball.x
    coords_ball.y += velocity_ball.y

    gr.time.sleep(0.05)

    update_acceleration()
    update_velocity_ball()


def move_fish(fish):
    if coords_ball.y >= SIZE_Y / 2:
        update_velocity_fish()

        for i in range(6):
            fish[i].move(velocity_fish.x, velocity_fish.y)

        coords_fish.x += velocity_fish.x
        coords_fish.y += velocity_fish.y

        gr.time.sleep(0.05)


def main(ball):
    while coords_ball.x - coords_fish.x >= 20:
        move_ball(ball, 'Red')
        check_walls()
        check_raft()
        check_floor()

        move_fish(fish)

    else:
        velocity_fish.x = 0
        velocity_fish.y = 0

        move_ball(ball, 'Navy')


decoration(w)

ball = gr.Circle(coords_ball, 20)
ball.draw(w)

main(ball)

remain_background(w)

w.getMouse()
w.close()
