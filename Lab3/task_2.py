import graphics as gr

window = gr.GraphWin("FIFA 2019", 800, 600)


back1 = gr.Rectangle(gr.Point(0,300), gr.Point(800,0))
back1.setFill('SkyBlue1')
back2 = gr.Rectangle(gr.Point(0, 600), gr.Point(800, 300))
back2.setFill('tan1')
back1.draw(window)
back2.draw(window)

#
# for i in range(5):
#     circle = gr.Circle(gr.Point(), size)
#     circle.setFill('White')
#     circle.draw(window)
#     x += size/2


stick=gr.Rectangle(gr.Point(80, 400), gr.Point(120, 100))
stick.setFill('salmon4')
stick.draw(window)

tree=gr.Oval(gr.Point(50,130), gr.Point(150,20))
tree.setFill('SpringGreen4')
tree.draw(window)

stick1=gr.Rectangle(gr.Point(180, 500), gr.Point(220, 200))
stick1.setFill('sienna4')
stick1.draw(window)

tree1=gr.Oval(gr.Point(150, 260), gr.Point(250,140))
tree1.setFill('OliveDrab4')
tree1.draw(window)

stick2=gr.Rectangle(gr.Point(640, 550), gr.Point(660, 250))
stick2.setFill('brown4')
stick2.draw(window)

tree2=gr.Circle(gr.Point(650, 250), 50)
tree2.setFill('green4')
tree2.draw(window)

Sun = gr.Circle(gr.Point(700,100), 80)
Sun.setFill('yellow')
Sun.draw(window)

pond = gr.Oval(gr.Point(300, 550), gr.Point(600, 450))
pond.setFill('blue2')
pond.draw(window)


window.getMouse()

window.close()
