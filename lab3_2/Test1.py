import graphics as gr

SIZE_X = 800
SIZE_Y = 600

window = gr.GraphWin("Model1", SIZE_X, SIZE_Y)
coord=gr.Point(100, 100)
def Telo():
    Ball = gr.Circle(coord, 30)
    Ball.setFill("Red")

    Ball.draw(window)


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


t = 0


while t <= 10:
    clear_window()
    Telo()
    Ball.move(10, 10)
    t += 1
    gr.time.sleep(0.2)


window.getMouse()

window.close()
