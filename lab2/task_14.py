import turtle as t


t.shape('turtle')
N=100
t.left(180)
def star(k,c):
    t.color(c)
    t.begin_fill()
    for i in range(k):
        t.forward(N)
        t.left(180-180/k)
    t.end_fill()
star(5, 'Yellow')
t.right(36)
t.penup()
t.goto(3*N,0)
t.pendown()
star(11, 'Red')
