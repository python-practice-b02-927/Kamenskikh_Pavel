from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
l = Label(bg='black', fg='white', width=20)
l.pack()
score = 0
s = 'Score: '

def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)

    canv.create_oval(x-r, y-r, x+r, y+r, fill = choice(colors), width=0)
    root.after(1000, new_ball)

    l['text'] = '' + s + str(score)


def click(event):
    global score
    if ((event.x - x) ** 2 + (event.y - y) ** 2) ** (1 / 2) <= r:
        score += 1
    else:
        canv.create_line(event.x - 5, event.y + 5, event.x + 5, event.y - 5, fill='red', width=3)
        canv.create_line(event.x + 5, event.y + 5, event.x - 5, event.y - 5, fill='red', width=3)


new_ball()
canv.bind('<Button-1>', click)
mainloop()