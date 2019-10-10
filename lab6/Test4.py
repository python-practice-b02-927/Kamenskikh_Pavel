from tkinter import *
from random import randrange as rnd, choice
import time
import json
from operator import itemgetter

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
l = Label(bg='black', fg='white', width=20)
l.pack()
score = 0
s = 'Score: '

All_Number = 0
Number_balls = 0
balls = []


def new_ball():
    global balls, All_Number, d
    All_Number += 1
    d = {}

    x = d['x'] = rnd(100, 700)
    y = d['y'] = rnd(100, 500)
    r = d['r'] = rnd(20, 40)

    d['color'] = choice(colors)
    d['v_y'] = rnd(-4, 4)
    d['v_x'] = rnd(-4, 4)

    a = All_Number % 30
    b = All_Number % 3
    if a == 0:
        d['id'] = canv.create_oval(x - r, y - r, x + r, y + r, fill='yellow', width=0)
        canv.create_arc(x - 0.6 * r, y - 0.6 * r, x + 0.6 * r, y + 0.6 * r,
                     start=220, extent=100, style=ARC, outline='red', width=5)
        canv.create_oval(x - 0.8 * r, y - 0.6 * r, x - 0.6 * r, y - 0.4 * r, fill='black', width=0)
        canv.create_oval(x + 0.8 * r, y - 0.6 * r, x + 0.6 * r, y - 0.4 * r, fill='black', width=0)
        d['shape'] = 'smile'
    elif b == 0:
        d['id'] = canv.create_rectangle(x - r, y - r, x + r, y + r, fill=d['color'], width=0)
        d['shape'] = 'rectangle'
    else:
        d['id'] = canv.create_oval(x - r, y - r, x + r, y + r, fill=d['color'], width=0)
        d['shape'] = 'circle'

    balls.append(d)

    root.after(2000, new_ball)
    l['text'] = '' + s + str(score)


def update_coords(i):
    check_walls(i)
    balls[i]['x'] += balls[i]['v_x']
    balls[i]['y'] += balls[i]['v_y']


def check_walls(i):
    if balls[i]['x'] >= 800 - balls[i]['r'] or balls[i]['x'] <= balls[i]['r']:
        balls[i]['v_x'] = - balls[i]['v_x']

    if balls[i]['y'] >= 600 - balls[i]['r'] or balls[i]['y'] <= balls[i]['r']:
        balls[i]['v_y'] = - balls[i]['v_y']


def move():
    canv.delete(ALL)
    Number_balls = len(balls)
    for i in range(Number_balls):
        update_coords(i)
        x = balls[i]['x']
        y = balls[i]['y']
        r = balls[i]['r']
        if balls[i]['shape'] == 'smile':
            canv.create_oval(x - r, y - r, x + r, y + r, fill='yellow', width=0)
            canv.create_arc(x - 0.6 * r, y - 0.6 * r, x + 0.6 * r, y + 0.6 * r,
                            start=220, extent=100, style=ARC, outline='red', width=5)
            canv.create_oval(x - 0.8 * r, y - 0.6 * r, x - 0.6 * r, y - 0.4 * r, fill='black', width=0)
            canv.create_oval(x + 0.8 * r, y - 0.6 * r, x + 0.6 * r, y - 0.4 * r, fill='black', width=0)
        elif balls[i]['shape'] == 'rectangle':
            canv.create_rectangle(x - r, y - r, x + r, y + r, fill=balls[i]['color'], width=0)
        else:
            canv.create_oval(x - r, y - r, x + r, y + r, fill=balls[i]['color'], width=0)
    root.after(20, move)


def click(event):
    global score
    delete = []

    for i in range(len(balls)):
        R = ((event.x - balls[i]['x']) ** 2 + (event.y - balls[i]['y']) ** 2) ** 0.5

        if R <= balls[i]['r'] and balls[i]['shape'] == 'circle':
            delete.append(i)
            score += 1

        if R <= balls[i]['r'] and balls[i]['shape'] == 'rectangle':
            delete.append(i)
            score += 10

        if R <= balls[i]['r'] and balls[i]['shape'] == 'smile':
            delete.append(i)
            score *= 20

    Number_balls = len(delete)
    for i in range(Number_balls):
        canv.delete(balls[delete[i]]['id'])
        del balls[delete[i]]


def main():
    new_ball()
    move()
    canv.bind('<Button-1>', click)


def results():
    liderscore_1 = {}
    nickname = input("Enter your nickname\n")
    with open('Lidership.json') as f:
        liderscore = json.load(f)
    if nickname in liderscore:
        if liderscore[nickname] < score:
            liderscore[nickname] = score
    else:
        liderscore[nickname] = score

    list_liders = list(liderscore.items())

    liderscore_sorted = sorted(list_liders, key=lambda i: i[1])

    liderscore_1 = dict(liderscore_sorted)

    with open('Lidership.json', 'w') as f:
        json.dump(liderscore_1, f, indent=1)


main()

mainloop()
results()