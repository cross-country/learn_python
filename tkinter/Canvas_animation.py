from tkinter import *

root =Tk()

def motion():
    x = event1
    y = event2
    z = can.coords(ball)[0]
    q = can.coords(ball)[1]
    if x > z:
        a = 1
    elif x < z:
        a = -1
    else:
        a = 0

    if y > q:
        b = 1
    elif y < q:
        b = -1
    else:
        b = 0
    if can.coords(ball)[0] != x:
        can.move(ball, a, 0)
        root.after(10, motion)
    elif can.coords(ball)[1] != y:
        can.move(ball, 0, b)
        root.after(5, motion)

def move_func(event):
    global event1
    global event2
    event1 = event.x
    event2 = event.y
    motion()




can = Canvas(width=400, height=250, bg='white')
can.pack()
can.bind('<Button-1>', move_func)

ball = can.create_oval(40,40,80,80, fill='green', outline='green')




root.mainloop()