import graphics as gr

window = gr.GraphWin("FIFA 2019", 400, 400)

def draw_background():
    back1 = gr.Rectangle(gr.Point(0,200), gr.Point(200,0))
    back1.setFill('Red')
    back2 = gr.Rectangle(gr.Point(0, 400), gr.Point(200, 200))
    back2.setFill('Green')
    back1.draw(window)
    back2.draw(window)

draw_background()


window.getMouse()

window.close()
