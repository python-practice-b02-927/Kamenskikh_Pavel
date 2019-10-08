from tkinter import *

root = Tk()


def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)


root.geometry('600x800')
e = Entry(root, width=20)
b = Button(root, text="OK")
l = Label(root, bg='black', fg='white', width=20)

e.pack()
b.pack()
l.pack()

b.bind('<Button-1>', strToSortlist)

mainloop()