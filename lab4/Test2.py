import graphics as gr


SIZE_X=600
SIZE_Y=800

def draw_snowman(win):
    

def draw_ice_hole(win):
    e1 = gr.Oval(gr.Point(300, 650), gr.Point(500, 550))
    e1.setFill("Grey")
    e1.setOutline("Grey")

    e2 = gr.Oval(gr.Point(SIZE_X*7/12, SIZE_Y*13/16), gr.Point(SIZE_X*3/4, SIZE_Y*3/4))
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
    pass


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