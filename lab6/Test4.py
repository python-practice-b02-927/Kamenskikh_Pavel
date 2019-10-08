from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
l = Label(bg='black', fg='white', width=20)
l.pack()
score = 0
s = 'Score: '

Number_balls = 0
balls = []
k = -1


def new_ball():
    global balls
    d = {}

    x =d['x'] = rnd(100, 700)
    y = d['y'] = rnd(100, 500)

    r = d['r'] = rnd(20, 40)

    d['color'] = choice(colors)
    d['v_y'] = rnd(-20, 20)
    d['v_x'] = rnd(-20, 20)

    d['id'] = canv.create_oval(x-r, y-r, x+r, y+r, fill = d['color'], width=0)

    balls.append(d)

    root.after(2000, new_ball)
    l['text'] = '' + s + str(score)


def update_coords(i):
    check_walls(i)
    balls[i]['x'] +=  balls[i]['v_x']
    balls[i]['y'] += balls[i]['v_y']


def check_walls(i):
    if balls[i]['x'] >= 800 or balls[i]['x'] <= 0 or balls[i]['y'] >= 600 or balls[i]['y'] <= 0:
        balls[i]['v_x'] = rnd(-20, 20)
        balls[i]['v_y'] = rnd(-20, 20)


def move():
    canv.delete(ALL)

    for i in range(len(balls)):
        update_coords(i)
        canv.create_oval(balls[i]['x'] - balls[i]['r'], balls[i]['y'] - balls[i]['r'], balls[i]['x'] + balls[i]['r'],
                         balls[i]['y'] + balls[i]['r'], fill = balls[i]['color'], width=0)
    root.after(1000, move)


def click(event):
    global score
    for i in range(len(balls)):
        if ((event.x - balls[i]['x']) ** 2 + (event.y - balls[i]['y']) ** 2) ** 0.5 <= balls[i]['r']:
            score += 1
            k = i
            break
    else:
        canv.create_line(event.x - 5, event.y + 5, event.x + 5, event.y - 5, fill='red', width=3)
        canv.create_line(event.x + 5, event.y + 5, event.x - 5, event.y - 5, fill='red', width=3)

    if k >= 0:
        elem = balls.pop(k)


def main():
    new_ball()
    move()
    canv.bind('<Button-1>', click)


main()

mainloop()