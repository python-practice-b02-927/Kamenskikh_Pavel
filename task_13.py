import turtle as t
import math


def circle(x, r, c):
	t.goto(x+r,x*x*r/3200)
	t.color(c)
	t.begin_fill()
	for i in range(360):
		t.goto(x+r*math.cos(math.pi*i/180), x*x*r/3200+r*math.sin(math.pi*i/180))
	t.end_fill()


t.shape('turtle')
t.penup()
circle(0, 200, "Yellow")
circle(-80, 40, "Blue")
circle(80, 40, "Blue")
t.goto(0,40)
t.pendown()
t.color('Black')
t.width(15)
t.goto(0,-40)
t.penup()
t.goto(120,-40)
t.pendown()
t.color('Red')
for i in range(180):
	t.goto(0 + 120 * math.cos(math.pi * i / 180), -40 - 120 * math.sin(math.pi * i / 180))


