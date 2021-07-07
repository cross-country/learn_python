from tkinter import *

root = Tk()

can = Canvas(root, width=500, height=500, bg='white')
can.pack()

can.create_oval(420,10,480,70, fill='yellow', outline='yellow')

can.create_line(250,400,250,80,fill='lightblue', width=200,
                arrow=LAST, arrowshape='150 150 50')


def grass(first, second):
    a = 1
    while a <= 15:
        can.create_arc(first, 420, second, 480, start=100, extent=80,
                       outline='darkgreen', width=4, style=ARC)
        first += 30
        second += 30
        a +=1


def grass_2(first, second):
    a = 1
    while a <= 15:
        can.create_line(first,500,second,440, fill='darkgreen', width=4)
        first +=30
        second +=30
        a +=1

#can.create_line(23,500,32, 440, fill='darkgreen', width=4)

grass(30, 90)
grass_2(23,32)



root.mainloop()