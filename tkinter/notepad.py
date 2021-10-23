from tkinter import *

root = Tk()

my_label = Label(fg='red')
my_label.pack()

f2 = Frame()
my_text = Text(f2, height=15, width=60, wrap=NONE)

def open_func():
    try:
        my_label['text'] = ""
        my_text.delete(1.0, END)
        a = ent.get()
        f = open(a, 'r')
        g = f.read()
        my_text.insert(1.0, g)
        f.close()
    except FileNotFoundError:
        my_text.delete(0.1, END)
        my_label['text'] = "Can`t find this file "
    except:
        my_text.delete(0.1, END)
        my_label['text'] = "Something went wrong "


def save_func():
    try:
        my_label['text'] = ""
        a = ent.get()
        f = open(a, 'w')
        g = my_text.get(1.0, END)
        f.write(g)
        f.close()
    except FileNotFoundError:
        my_label['text'] = "Wrong filename"



head = Frame(width=60)
ent = Entry(head, width=20)
btn_1 = Button(head, width=10, text='open')
btn_1['command'] = open_func
btn_2 = Button(head, width=10, text='save')
btn_2['command'] = save_func


head.pack(anchor=NW)
ent.pack(side=LEFT, padx=3, pady=3)
btn_1.pack(side=LEFT, padx=3, pady=3)
btn_2.pack(side=LEFT, padx=3, pady=3)


f2.pack()

my_text.pack(side=LEFT, expand=1, fill=BOTH)

right_scroll = Scrollbar(f2, command=my_text.yview)
right_scroll.pack(side=LEFT)


bottom_scroll = Scrollbar(orient=HORIZONTAL, command=my_text.xview)
bottom_scroll.pack(side=BOTTOM, fill=X)

my_text.config(yscrollcommand=right_scroll.set)
my_text.config(xscrollcommand=bottom_scroll.set)





root.mainloop()


