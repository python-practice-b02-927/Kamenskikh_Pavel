from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
l = Label(bg='black', fg='white', width=20)
l.pack()
score = 0
s = 'Score: '

balls = []

def new_ball():
    global balls
    d = {}

    x =d['x'] = rnd(100, 700)
    y = d['y'] = rnd(100, 500)

    r = d['r'] = rnd(30, 50)
    d['v_y'] = rnd(0, 20)

    d['v_x'] = rnd(0, 20)
    d['id'] = canv.create_oval(x-r, y-r, x+r, y+r, fill = choice(colors), width=0)

    balls.append(d)

    root.after(1000, new_ball)

    l['text'] = '' + s + str(score)


def update_velocity(i):
    balls[i['x']] = + balls[i['v_x']]
    balls[i['y']] = + balls[i['v_y']]


#def click(event, i):
 #   global score
  #  if ((event.x - balls[i['x']]) ** 2 + (event.y - balls[i['y']]) ** 2) ** (1 / 2) <= balls[i['r']]:
   #     score += 1
    #else:
    #    canv.create_line(event.x - 5, event.y + 5, event.x + 5, event.y - 5, fill='red', width=3)
     #   canv.create_line(event.x + 5, event.y + 5, event.x - 5, event.y - 5, fill='red', width=3)

def main():
    new_ball()
    #canv.bind('<Button-1>', click)

main()

mainloop()