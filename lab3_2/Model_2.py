import graphics as gr

SIZE_X=800
SIZE_Y=600

w = gr.GraphWin("Resistance", SIZE_X, SIZE_Y)
coords = gr.Point(100, 500)
acceleration_g = 1
velocity = gr.Point(20, -40)
k = -0.1
acceleration_k = gr.Point(0,0)


def draw_background(w):
    r1 = gr.Rectangle(gr.Point(0,0), gr.Point(SIZE_X, SIZE_Y*2/3))
    r1.setFill('Blue')
    r1.setOutline(('Blue'))
    r2 = gr.Rectangle(gr.Point(0, SIZE_Y*2/3), gr.Point(SIZE_X, SIZE_Y))
    r2.setFill('Green')
    r2.setOutline(('Green'))

    r1.draw(w)
    r2.draw(w)

    #def football(x,y):
     #   football = gr.Polygon(gr.Point(x,y))
      #  football.setFill('Black')
       #football.draw(w)


def draw_reed(x,y):
    reed_1 = gr.Rectangle(gr.Point(x,y), gr.Point(x+5, y-150))
    reed_1.setFill('Brown')
    reed_1.setOutline('Brown')
    reed_2 = gr.Oval(gr.Point(x-3, y-145), gr.Point(x+8, y-195))
    reed_2.setFill('Black')

    reed_1.draw(w)
    reed_2.draw(w)


def draw_sun():
    sun = gr.Circle( gr.Point(200, 100), 40)
    sun.setFill("Yellow")
    sun.setOutline('Orange')

    sun.draw(w)


def draw_lake():
    lake = gr.Oval(gr.Point(400,550), gr.Point(650, 450))
    lake.setFill('Blue')
    lake.setOutline('Blue')
    x = 650
    y = 500
    for i in range(7):
        draw_reed(x, y)
        x=x+15
        y=y+40*(-1)**i
    lake.draw(w)


def update_acceleration():
    acceleration_k.x = k*velocity.x
    acceleration_k.y = k*velocity.y


def update_velocity():
    velocity.y = velocity.y + acceleration_g + acceleration_k.y
    velocity.x = velocity.x + acceleration_k.x


def check_walls():
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -1 * velocity.x
        acceleration_k.x = -1 * acceleration_k.x

    if coords.y > SIZE_Y:
        velocity.y = (-1) * velocity.y
        acceleration_k.y = (-1) * acceleration_k.y

def check_ground():
    if coords.y > 500 and coords.x > 400 and coords.x < 650:
        velocity.x = 0
        velocity.y = 0
        update_acceleration()
        ball.setFill('Blue')
        ball.setOutline('Blue')
    elif coords.y > 500:
        velocity.x = 0
        velocity.y = 0
        update_acceleration()



def move():
    ball.move(velocity.x, velocity.y)
    coords.x = coords.x + velocity.x
    coords.y = coords.y + velocity.y
    gr.time.sleep(0.2)
    update_acceleration()
    update_velocity()
    check_walls()
    check_ground()



def decoration(w):
    draw_background(w)
    draw_lake()
    draw_sun()

decoration(w)
ball = gr.Circle(coords, 20)
ball.setFill('Red')
ball.setOutline('Red')

ball.draw(w)
t = 1

while t <= 100:
    move()
    t = t + 1

w.getMouse()
w.close()
