from tkinter import *
from random import random

root = Tk()
root.geometry('1000x700')

def shift():
    x = round(random(), 2) - 0.05
    y = round(random(), 2) - 0.05
    btn.place(relx=x, rely=y)


img = PhotoImage(file='finger2.gif')

btn = Button(bg='green', image=img, command=shift)
btn.place(relx=0.4, rely=0.05)


root.mainloop()