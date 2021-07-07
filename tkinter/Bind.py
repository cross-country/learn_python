from tkinter import *

root = Tk()

def add_func(event):
    a = ent.get()
    list.insert(END, a)
    ent.delete(0, END)

def in_func(event):
    ent.delete(0, END)
    b = list.curselection()
    for i in b:
        c = list.get(i)
        ent.insert(0, c)

but = Button(text="button")
but.bind('<Button-1>', in_func)
but.pack()


ent = Entry()
ent.bind('<Return>', add_func)
ent.pack(padx=5, pady=2)

list = Listbox()
list.bind('<Double-Button-1>', in_func)
list.pack(pady=3)




root.mainloop()