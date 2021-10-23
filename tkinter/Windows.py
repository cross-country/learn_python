from tkinter import *

root = Tk()

def add_item(event):
    def create(event2):
        x1 = int(ent1.get())
        y1 = int(ent2.get())
        x2 = int(ent3.get())
        y2 = int(ent4.get())

        if my_var.get() == 0:
            can.create_rectangle(x1,y1,x2,y2, fill='green')
            print(x1)
        elif my_var.get() == 1:
            can.create_oval(x1,y1,x2,y2, fill='red')
        else:
            print('No')
        top.after(1000, lambda: top.destroy())



    top = Toplevel()
    top.geometry('200x200+500+20')

    f1 = Frame(top)
    f1.pack()

    f2 = Frame(top)
    f2.pack()

    my_var = IntVar()
    my_var.set(0)

    r1 = Radiobutton(top, text='rectangle', variable=my_var, value=0)
    r1.pack(padx=10)

    r2 = Radiobutton(top, text='circus', variable=my_var, value=1)
    r2.pack(ipadx=0)

    btn1 = Button(top, width=10, text='create')
    btn1.pack()
    btn1.bind('<Button-1>', create)

    lab1 = Label(f1, text='x1')
    lab1.pack(side=LEFT)

    ent1 = Entry(f1, width=4)
    ent1.pack(side=LEFT)

    lab2 = Label(f1, text='y1')
    lab2.pack(side=LEFT)

    ent2 = Entry(f1, width=4)
    ent2.pack(side=LEFT)

    lab3 = Label(f2, text='x2')
    lab3.pack(side=LEFT)

    ent3 = Entry(f2, width=4)
    ent3.pack(side=LEFT)

    lab4 = Label(f2, text='y2')
    lab4.pack(side=LEFT)

    ent4 = Entry(f2, width=4)
    ent4.pack(side=LEFT)



can = Canvas(width=400, height=400)
can.pack()


btn = Button(width=10, text='Create')
btn.pack()
btn.bind('<Button-1>', add_item )







root.mainloop()