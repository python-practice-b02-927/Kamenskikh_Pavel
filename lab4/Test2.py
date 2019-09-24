import graphics as gr


SIZE_X = 600
SIZE_Y = 600

def draw_body_fish():
    e3 = gr.Oval(gr.Point(400, 550), gr.Point(480, 500))
    e3.setFill("Yellow")
    e3.setOutline("Yellow")
    e3.draw(w)





def draw_snowman(win):
    pass


def draw_ice_hole(win):
    e1 = gr.Oval(gr.Point(300, 450), gr.Point(500, 350))
    e1.setFill("Black")
    e1.setOutline("Black")

    e2 = gr.Oval(gr.Point(350, 450), gr.Point(450, 400))
    e2.setFill("Blue")
    e2.setOutline("Blue")

    e1.draw(w)
    e2.draw(w)


def draw_fishing_rod(win):
    pass


def draw_background(win):
    r1 = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y/2))
    r1.setFill("Blue")
    r1.setOutline('Blue')
    r2 = gr.Rectangle(gr.Point(0, SIZE_Y/2), gr.Point(SIZE_X, SIZE_Y))
    r2.setFill("White")
    r2.setOutline('White')

    r1.draw(w)
    r2.draw(w)


def draw_fish(win):
    draw_body_fish()

    t1 = gr.Polygon(gr.Point(400, 525), gr.Point(370, 480), gr.Point(360, 580))
    t1.setFill("Yellow")
    t1.setOutline("Yellow")
    t1.draw(w)

    eye = gr.Circle(gr.Point(460, 520), 5)
    eye.setFill("Black")
    eye.setOutline("Black")


    eye.draw((w))



def draw_star(win):
    pass


def main(win):
    """Draws picture"""
    draw_snowman(win)
    draw_ice_hole(win)
    draw_fishing_rod(win)
    draw_background(win)
    draw_fish(win)
    draw_star(win)


w = gr.GraphWin('pic9_1', SIZE_X, SIZE_Y)

main(w)
w.getMouse()
w.close()